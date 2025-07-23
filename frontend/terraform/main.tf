provider "aws" {
  alias  = "us_east_1"
  region = "us-east-1"
}


data "aws_route53_zone" "selected" {
  name = var.zone_name
}

data "aws_acm_certificate" "wildcard" {
  provider    = aws.us_east_1
  domain      = "*.${var.zone_name}"
  statuses    = ["ISSUED"]
  most_recent = true
}

# Remote states for other services

data "terraform_remote_state" "spotify" {
  backend = "s3"
  config = {
    bucket = "ctbus-tfstates"
    key    = "ctbus_site/spotify.tfstate"
    region = "us-east-1"
  }
}

data "terraform_remote_state" "assets" {
  backend = "s3"
  config = {
    bucket = "ctbus-tfstates"
    key    = "ctbus_site/assets.tfstate"
    region = "us-east-1"
  }
}

resource "aws_s3_bucket" "this" {
  bucket = local.bucket_name
}

locals {
  env         = terraform.workspace
  bucket_name = "${var.bucket_name}-${local.env}"
  hostname    = local.env == "main" ? "charliebushman.com" : "${local.env}.charliebushman.com"
  env_aliases = local.env == "main" ? ["www.charliebushman.com"] : []
  site_dir    = "${path.root}/../src"
  site_files  = fileset(local.site_dir, "**")
  placeholders = {
    "SPOTIFY_PLAYLISTS_URL" = data.terraform_remote_state.spotify.outputs.spotify_playlists_url
    "ASSETS_BASE_URL"       = "https://${data.terraform_remote_state.assets.outputs.domain_name}"
    "ENV_NAME"              = local.env
  }
  processed_files = {
    for f in local.site_files :
    f => replace(
      replace(
        replace(
          file("${local.site_dir}/${f}"),
          "SPOTIFY_PLAYLISTS_URL",
          local.placeholders["SPOTIFY_PLAYLISTS_URL"]
        ),
        "ASSETS_BASE_URL",
        local.placeholders["ASSETS_BASE_URL"]
      ),
      "ENV_NAME",
      local.placeholders["ENV_NAME"]
    )
  }
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
  aliases = distinct(concat([local.hostname], var.additional_aliases, local.env_aliases))
}

resource "aws_s3_object" "site" {
  for_each = local.processed_files
  bucket   = aws_s3_bucket.this.id
  key      = each.key
  content  = each.value
  content_type = lookup(
    local.mime_types,
    lower(element(reverse(split(".", each.key)), 0)),
    "text/plain",
  )
  etag = md5(each.value)
}

resource "aws_cloudfront_origin_access_identity" "this" {
  comment = "Website access"
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

resource "aws_cloudfront_function" "spa_rewrite" {
  name    = "${local.bucket_name}-spa-rewrite"
  runtime = "cloudfront-js-1.0"
  publish = true
  code    = file("${path.module}/spa-redirect.js")
}

resource "aws_cloudfront_distribution" "this" {
  enabled             = true
  default_root_object = "index.html"
  aliases             = local.aliases

  origin {
    domain_name = aws_s3_bucket.this.bucket_regional_domain_name
    origin_id   = "s3-frontend"
    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.this.cloudfront_access_identity_path
    }
  }

  default_cache_behavior {
    target_origin_id       = "s3-frontend"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD", "OPTIONS"]

    function_association {
      event_type   = "viewer-request"
      function_arn = aws_cloudfront_function.spa_rewrite.arn
    }

    forwarded_values {
      query_string = false
      cookies { forward = "none" }
    }
  }

  dynamic "custom_error_response" {
    for_each = {
      403 = { response_code = 404, response_page_path = "/404.html" }
      404 = { response_code = 404, response_page_path = "/404.html" }
      500 = { response_code = 500, response_page_path = "/50x.html" }
      502 = { response_code = 500, response_page_path = "/50x.html" }
      503 = { response_code = 500, response_page_path = "/50x.html" }
      504 = { response_code = 500, response_page_path = "/50x.html" }
    }
    content {
      error_code         = custom_error_response.key
      response_code      = custom_error_response.value.response_code
      response_page_path = custom_error_response.value.response_page_path
    }
  }

  price_class = "PriceClass_100"
  viewer_certificate {
    acm_certificate_arn      = data.aws_acm_certificate.wildcard.arn
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
  for_each = toset(local.aliases)
  zone_id  = data.aws_route53_zone.selected.zone_id
  name     = each.value
  type     = "A"

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
  value = local.aliases[0]
}
