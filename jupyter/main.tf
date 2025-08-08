provider "aws" {
  region = "us-east-1"
}

data "aws_route53_zone" "selected" {
  name = var.zone_name
}

resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
}

locals {
  dist_dir  = "${path.root}/dist"
  dist_files = fileset(local.dist_dir, "**")
  mime_types = {
    html = "text/html"
    js   = "application/javascript"
    css  = "text/css"
    json = "application/json"
    png  = "image/png"
    gif  = "image/gif"
    ico  = "image/x-icon"
    pdf  = "application/pdf"
    txt  = "text/plain"
    ipynb = "application/x-ipynb+json"
    py = "text/x-python"
    webmanifest = "application/manifest+json"
    whl = "application/zip"
    Snakefile = "text/x-snakefile"
    smk = "text/x-snakefile"
    yaml = "application/x-yaml"
  }

  alias = var.hostname
}

resource "aws_s3_object" "asset" {
  for_each     = { for f in local.dist_files : f => f }
  bucket       = aws_s3_bucket.this.id
  key          = each.key
  source       = "${local.dist_dir}/${each.value}"
  content_type = lookup(local.mime_types, lower(element(reverse(split(".", each.key)), 0)), "binary/octet-stream")
  source_hash  = filesha256("${local.dist_dir}/${each.value}")
}

resource "aws_cloudfront_origin_access_identity" "this" {
  comment = "Jupyter access"
}

data "aws_iam_policy_document" "allow_cloudfront" {
  statement {
    actions   = ["s3:GetObject"]
    resources = ["${aws_s3_bucket.this.arn}/*"]
    principals {
      type        = "AWS"
      identifiers = [aws_cloudfront_origin_access_identity.this.iam_arn]
    }
  }
}

resource "aws_s3_bucket_policy" "allow_cloudfront" {
  bucket = aws_s3_bucket.this.id
  policy = data.aws_iam_policy_document.allow_cloudfront.json
}

resource "aws_cloudfront_distribution" "this" {
  enabled             = true
  default_root_object = "index.html"
  aliases             = [local.alias]

  origin {
    domain_name = aws_s3_bucket.this.bucket_regional_domain_name
    origin_id   = "jupyter-bucket"
    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.this.cloudfront_access_identity_path
    }
  }

  default_cache_behavior {
    target_origin_id       = "jupyter-bucket"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD", "OPTIONS"]
    forwarded_values {
      query_string = false
      cookies { forward = "none" }
    }
  }

  price_class = "PriceClass_100"
  viewer_certificate {
    acm_certificate_arn      = var.certificate_arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2021"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }
}

resource "aws_route53_record" "cdn" {
  zone_id = data.aws_route53_zone.selected.zone_id
  name    = local.alias
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.this.domain_name
    zone_id                = aws_cloudfront_distribution.this.hosted_zone_id
    evaluate_target_health = false
  }
}

output "bucket_name" {
  value = aws_s3_bucket.this.bucket
}

output "cloudfront_domain" {
  value = aws_cloudfront_distribution.this.domain_name
}

output "domain_name" {
  value = local.alias
}
