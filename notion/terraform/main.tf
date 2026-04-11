provider "aws" {
  region = "us-east-1"
}

# ---------------------------------------------------------------------------
# Build Lambda package
# ---------------------------------------------------------------------------

resource "null_resource" "lambda_build" {
  triggers = {
    handler      = filemd5("${path.module}/../lambda/handler.py")
    requirements = filemd5("${path.module}/../lambda/requirements.txt")
  }

  provisioner "local-exec" {
    command = <<-EOT
      rm -rf ${path.module}/../lambda/package
      pip install -r ${path.module}/../lambda/requirements.txt \
        -t ${path.module}/../lambda/package/ --quiet --upgrade
      cp ${path.module}/../lambda/handler.py ${path.module}/../lambda/package/
    EOT
  }
}

data "archive_file" "notion_automations" {
  type        = "zip"
  source_dir  = "${path.module}/../lambda/package"
  output_path = "${path.module}/../lambda/notion-automations.zip"
  depends_on  = [null_resource.lambda_build]
}

# ---------------------------------------------------------------------------
# IAM
# ---------------------------------------------------------------------------

resource "aws_iam_role" "notion_automations" {
  name = "notion-automations-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "notion_automations_basic" {
  role       = aws_iam_role.notion_automations.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# ---------------------------------------------------------------------------
# Lambda
# ---------------------------------------------------------------------------

resource "aws_lambda_function" "notion_automations" {
  function_name    = "notion-automations"
  role             = aws_iam_role.notion_automations.arn
  handler          = "handler.handler"
  runtime          = "python3.12"
  filename         = data.archive_file.notion_automations.output_path
  source_code_hash = data.archive_file.notion_automations.output_base64sha256
  timeout          = 60

  environment {
    variables = {
      NOTION_TOKEN              = var.notion_token
      NOTION_AUTOMATIONS_DB_ID  = var.notion_automations_db_id
      NOTION_TASKS_DB_ID        = var.notion_tasks_db_id
    }
  }
}

# ---------------------------------------------------------------------------
# EventBridge — daily at 3am EST (8am UTC)
# ---------------------------------------------------------------------------

resource "aws_cloudwatch_event_rule" "notion_automations_daily" {
  name                = "notion-automations-daily"
  schedule_expression = "cron(0 8 * * ? *)"
}

resource "aws_cloudwatch_event_target" "notion_automations" {
  rule      = aws_cloudwatch_event_rule.notion_automations_daily.name
  target_id = "NotionAutomations"
  arn       = aws_lambda_function.notion_automations.arn
}

resource "aws_lambda_permission" "notion_automations_eventbridge" {
  statement_id  = "AllowEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.notion_automations.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.notion_automations_daily.arn
}
