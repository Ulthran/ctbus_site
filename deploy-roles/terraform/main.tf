provider "aws" {
  region = var.region
}

locals {
  services = {
    assets      = "Assets terraform apply role"
    frontend    = "Frontend terraform apply role"
    jupyter     = "Jupyter terraform apply role"
    maintenance = "Maintenance terraform apply role"
    spotify     = "Spotify terraform apply role"
  }

  environment_refs = ["refs/heads/master", "refs/heads/main"]
}

resource "aws_iam_openid_connect_provider" "github" {
  url             = "https://token.actions.githubusercontent.com"
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
}

data "aws_iam_policy_document" "assume_role" {
  for_each = local.services

  statement {
    actions = ["sts:AssumeRoleWithWebIdentity"]
    effect  = "Allow"

    principals {
      type        = "Federated"
      identifiers = [aws_iam_openid_connect_provider.github.arn]
    }

    condition {
      test     = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values   = ["sts.amazonaws.com"]
    }

    condition {
      test     = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values = [
        for ref in local.environment_refs : "repo:${var.github_owner}/${var.repository}:ref:${ref}"
      ]
    }
  }
}

resource "aws_iam_role" "deploy" {
  for_each = local.services

  name                 = "${var.role_name_prefix}-${each.key}-deploy"
  description          = each.value
  assume_role_policy   = data.aws_iam_policy_document.assume_role[each.key].json
  max_session_duration = 3600
}

resource "aws_iam_role_policy_attachment" "deploy_admin" {
  for_each = aws_iam_role.deploy

  role       = each.value.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

output "role_arns" {
  description = "Map of service identifiers to IAM role ARNs"
  value       = { for key, role in aws_iam_role.deploy : key => role.arn }
}
