provider "aws" {
  region = "us-east-1"
}

data "aws_route53_zone" "selected" {
  name = var.zone_name
}


resource "aws_s3_bucket" "this" {
  #checkov:skip=CKV_AWS_145:KMS encryption for S3 is overkill for a personal portfolio site
  bucket = var.bucket_name
}

resource "aws_s3_bucket_public_access_block" "this" {
  bucket = aws_s3_bucket.this.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "this" {
  bucket = aws_s3_bucket.this.id

  rule {
    id     = "expire-old-versions"
    status = "Enabled"

    noncurrent_version_expiration {
      noncurrent_days = 90
    }
  }
}

locals {
  assets_dir  = "${path.root}/../files"
  asset_files = fileset(local.assets_dir, "**")
  mime_types = {
    html = "text/html"
    js   = "application/javascript"
    css  = "text/css"
    vue  = "text/plain"
    json = "application/json"
    png  = "image/png"
    gif  = "image/gif"
    ico  = "image/x-icon"
    pdf  = "application/pdf"
    pptx = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    txt  = "text/plain"
    dtd  = "application/xml-dtd"
    nb   = "text/plain"
  }

  alias = var.hostname
}

resource "aws_s3_object" "asset" {
  for_each     = { for f in local.asset_files : f => f }
  bucket       = aws_s3_bucket.this.id
  key          = each.key
  source       = "${local.assets_dir}/${each.value}"
  content_type = lookup(local.mime_types, lower(element(reverse(split(".", each.key)), 0)), "binary/octet-stream")
  source_hash  = filesha256("${local.assets_dir}/${each.value}")
}

resource "aws_cloudfront_origin_access_identity" "this" {
  comment = "Assets access"
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

resource "aws_cloudfront_response_headers_policy" "security_headers" {
  name = "${var.bucket_name}-security-headers"

  security_headers_config {
    strict_transport_security {
      access_control_max_age_sec = 31536000
      include_subdomains         = true
      override                   = true
    }
    content_type_options {
      override = true
    }
    frame_options {
      frame_option = "DENY"
      override     = true
    }
    xss_protection {
      mode_block = true
      protection = true
      override   = true
    }
  }
}

resource "aws_cloudfront_distribution" "this" {
  #checkov:skip=CKV_AWS_86:CloudFront access logging not required for a personal portfolio
  enabled             = true
  default_root_object = "index.html"
  aliases             = [local.alias]

  origin {
    domain_name = aws_s3_bucket.this.bucket_regional_domain_name
    origin_id   = "assets-bucket"
    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.this.cloudfront_access_identity_path
    }
  }

  default_cache_behavior {
    target_origin_id           = "assets-bucket"
    viewer_protocol_policy     = "redirect-to-https"
    allowed_methods            = ["GET", "HEAD", "OPTIONS"]
    cached_methods             = ["GET", "HEAD", "OPTIONS"]
    response_headers_policy_id = aws_cloudfront_response_headers_policy.security_headers.id
    forwarded_values {
      query_string = false
      cookies { forward = "none" }
    }
  }

  price_class = "PriceClass_100"
  viewer_certificate {
    acm_certificate_arn      = var.certificate_arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2025"
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
