provider "aws" {
  region = "us-east-1"
}

data "archive_file" "spotify_playlists" {
  type        = "zip"
  source_file = "${path.module}/../lambda/index.js"
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

output "spotify_playlists_url" {
  value = aws_lambda_function_url.spotify_playlists.function_url
}
