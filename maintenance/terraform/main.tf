provider "aws" {
  region = "us-east-1"
}

data "archive_file" "maintenance" {
  type        = "zip"
  source_file = "${path.module}/../lambda/index.js"
  output_path = "${path.module}/../lambda/maintenance.zip"
}

resource "aws_iam_role" "maintenance_lambda" {
  name = "maintenance-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "maintenance_lambda_basic" {
  role       = aws_iam_role.maintenance_lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "maintenance" {
  function_name    = "maintenance"
  role             = aws_iam_role.maintenance_lambda.arn
  handler          = "index.handler"
  runtime          = "nodejs20.x"
  filename         = data.archive_file.maintenance.output_path
  source_code_hash = data.archive_file.maintenance.output_base64sha256
}

resource "aws_lambda_function_url" "maintenance" {
  function_name      = aws_lambda_function.maintenance.arn
  authorization_type = "NONE"
}

resource "aws_lambda_permission" "maintenance_url" {
  statement_id           = "AllowPublicAccess"
  action                 = "lambda:InvokeFunctionUrl"
  function_name          = aws_lambda_function.maintenance.function_name
  principal              = "*"
  function_url_auth_type = aws_lambda_function_url.maintenance.authorization_type
}

output "maintenance_url" {
  value = aws_lambda_function_url.maintenance.function_url
}
