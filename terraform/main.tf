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

resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
}


locals {
  site_dir    = "${path.root}/../vue-frontend"
  assets_dir  = "${path.root}/../assets"
  site_files  = fileset(local.site_dir, "**")
  asset_files = fileset(local.assets_dir, "**")
  placeholders = {
    "SPOTIFY_PLAYLISTS_URL" = aws_lambda_function_url.spotify_playlists.function_url
  }

  dev_placeholders = {
    "SPOTIFY_PLAYLISTS_URL" = length(aws_lambda_function_url.spotify_playlists_dev) > 0 ? aws_lambda_function_url.spotify_playlists_dev[0].function_url : ""
  }

  processed_files = {
    for f in local.site_files :
    f => replace(
      file("${local.site_dir}/${f}"),
      "SPOTIFY_PLAYLISTS_URL",
      local.placeholders["SPOTIFY_PLAYLISTS_URL"]
    )
  }

  dev_processed_files = {
    for f in local.site_files :
    f => replace(
      file("${local.site_dir}/${f}"),
      "SPOTIFY_PLAYLISTS_URL",
      local.dev_placeholders["SPOTIFY_PLAYLISTS_URL"]
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

  aliases     = concat([var.hostname], var.additional_aliases)
  dev_aliases = var.dev_hostname != "" ? [var.dev_hostname] : []
}

data "archive_file" "spotify_playlists" {
  type        = "zip"
  source_file = "${path.module}/../lambda/spotify-playlists/index.js"
  output_path = "${path.module}/../lambda/spotify-playlists.zip"
}

resource "aws_iam_role" "spotify_lambda" {
  name = "spotify-playlists-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "spotify_lambda_basic" {
  role       = aws_iam_role.spotify_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "spotify_playlists" {
  function_name    = "spotify-playlists"
  role             = aws_iam_role.spotify_lambda.arn
  handler          = "index.handler"
  runtime          = "nodejs20.x"
  filename         = data.archive_file.spotify_playlists.output_path
  source_code_hash = data.archive_file.spotify_playlists.output_base64sha256
  timeout          = 15
  environment {
    variables = {
      SPOTIFY_CLIENT_ID     = var.spotify_client_id
      SPOTIFY_CLIENT_SECRET = var.spotify_client_secret
    }
  }
}

resource "aws_lambda_function_url" "spotify_playlists" {
  function_name      = aws_lambda_function.spotify_playlists.arn
  authorization_type = "NONE"
}

resource "aws_lambda_permission" "spotify_playlists_url" {
  statement_id           = "AllowPublicAccess"
  action                 = "lambda:InvokeFunctionUrl"
  function_name          = aws_lambda_function.spotify_playlists.function_name
  principal              = "*"
  function_url_auth_type = aws_lambda_function_url.spotify_playlists.authorization_type
}

resource "aws_lambda_function" "spotify_playlists_dev" {
  count            = var.dev_hostname != "" ? 1 : 0
  function_name    = "spotify-playlists-dev"
  role             = aws_iam_role.spotify_lambda.arn
  handler          = "index.handler"
  runtime          = "nodejs20.x"
  filename         = data.archive_file.spotify_playlists.output_path
  source_code_hash = data.archive_file.spotify_playlists.output_base64sha256
  timeout          = 15
  environment {
    variables = {
      SPOTIFY_CLIENT_ID     = var.spotify_client_id
      SPOTIFY_CLIENT_SECRET = var.spotify_client_secret
    }
  }
}

resource "aws_lambda_function_url" "spotify_playlists_dev" {
  count              = var.dev_hostname != "" ? 1 : 0
  function_name      = aws_lambda_function.spotify_playlists_dev[0].arn
  authorization_type = "NONE"
}

resource "aws_lambda_permission" "spotify_playlists_url_dev" {
  count                  = var.dev_hostname != "" ? 1 : 0
  statement_id           = "AllowPublicAccessDev"
  action                 = "lambda:InvokeFunctionUrl"
  function_name          = aws_lambda_function.spotify_playlists_dev[0].function_name
  principal              = "*"
  function_url_auth_type = aws_lambda_function_url.spotify_playlists_dev[0].authorization_type
}

resource "aws_s3_object" "site" {
  for_each = local.processed_files
  bucket   = aws_s3_bucket.this.id
  key      = "frontend/${each.key}"
  content  = each.value
  content_type = lookup(
    local.mime_types,
    lower(element(reverse(split(".", each.key)), 0)),
    "text/plain",
  )
  etag = md5(each.value)
}

resource "aws_s3_object" "dev_site" {
  for_each = var.dev_hostname != "" ? local.dev_processed_files : {}
  bucket   = aws_s3_bucket.this.id
  key      = "dev/${each.key}"
  content  = each.value
  content_type = lookup(
    local.mime_types,
    lower(element(reverse(split(".", each.key)), 0)),
    "text/plain",
  )
  etag = md5(each.value)
}

resource "aws_s3_object" "asset" {
  for_each = { for f in local.asset_files : f => f }
  bucket   = aws_s3_bucket.this.id
  key      = "assets/${each.key}"
  source   = "${local.assets_dir}/${each.value}"
  content_type = lookup(
    local.mime_types,
    lower(element(reverse(split(".", each.key)), 0)),
    "binary/octet-stream",
  )
  source_hash = filesha256("${local.assets_dir}/${each.value}")
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
  name    = "${var.bucket_name}-spa-rewrite"
  runtime = "cloudfront-js-1.0"
  publish = true
  code    = file("${path.module}/spa-redirect-prod.js")
}

resource "aws_cloudfront_function" "spa_rewrite_dev" {
  count   = var.dev_hostname != "" ? 1 : 0
  name    = "${var.bucket_name}-dev-spa-rewrite"
  runtime = "cloudfront-js-1.0"
  publish = true
  code    = file("${path.module}/spa-redirect-dev.js")
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

resource "aws_cloudfront_distribution" "dev" {
  count               = var.dev_hostname != "" ? 1 : 0
  enabled             = true
  default_root_object = "index.html"
  aliases             = local.dev_aliases

  origin {
    domain_name = aws_s3_bucket.this.bucket_regional_domain_name
    origin_id   = "s3-frontend-dev"
    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.this.cloudfront_access_identity_path
    }
  }

  default_cache_behavior {
    target_origin_id       = "s3-frontend-dev"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD", "OPTIONS"]

    function_association {
      event_type   = "viewer-request"
      function_arn = aws_cloudfront_function.spa_rewrite_dev[0].arn
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

resource "aws_route53_record" "cdn_dev" {
  count   = var.dev_hostname != "" ? 1 : 0
  zone_id = data.aws_route53_zone.selected.zone_id
  name    = var.dev_hostname
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.dev[0].domain_name
    zone_id                = aws_cloudfront_distribution.dev[0].hosted_zone_id
    evaluate_target_health = false
  }
}

output "bucket_name" {
  value = aws_s3_bucket.this.bucket
}


output "cloudfront_domain" {
  value = aws_cloudfront_distribution.this.domain_name
}

output "cloudfront_domain_dev" {
  value       = var.dev_hostname != "" ? aws_cloudfront_distribution.dev[0].domain_name : null
  description = "Dev CloudFront distribution domain"
}

output "spotify_playlists_url" {
  value = aws_lambda_function_url.spotify_playlists.function_url
}

output "spotify_playlists_url_dev" {
  value       = var.dev_hostname != "" ? aws_lambda_function_url.spotify_playlists_dev[0].function_url : null
  description = "Dev playlists lambda URL"
}
