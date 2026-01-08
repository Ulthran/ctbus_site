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

data "aws_iam_policy_document" "assets_deploy" {
  statement {
    sid = "CreateAssetsBucket"

    actions = [
      "s3:CreateBucket",
      "s3:ListAllMyBuckets"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ManageAssetsBucket"

    actions = [
      "s3:*"
    ]

    resources = [
      "arn:aws:s3:::ctbus-site-assets",
      "arn:aws:s3:::ctbus-site-assets/*"
    ]
  }

  statement {
    sid = "ManageAssetsCloudFront"

    actions = [
      "cloudfront:CreateCloudFrontOriginAccessIdentity",
      "cloudfront:CreateDistribution",
      "cloudfront:DeleteCloudFrontOriginAccessIdentity",
      "cloudfront:DeleteDistribution",
      "cloudfront:GetCloudFrontOriginAccessIdentity",
      "cloudfront:GetCloudFrontOriginAccessIdentityConfig",
      "cloudfront:GetDistribution",
      "cloudfront:GetDistributionConfig",
      "cloudfront:ListTagsForResource",
      "cloudfront:TagResource",
      "cloudfront:UntagResource",
      "cloudfront:UpdateCloudFrontOriginAccessIdentity",
      "cloudfront:UpdateDistribution"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ListAssetsHostedZone"

    actions = [
      "route53:ListHostedZonesByName"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ManageAssetsDNS"

    actions = [
      "route53:ChangeResourceRecordSets",
      "route53:GetHostedZone",
      "route53:ListResourceRecordSets"
    ]

    resources = ["arn:aws:route53:::hostedzone/*"]
  }
}

resource "aws_iam_role_policy" "assets_deploy" {
  name   = "assets-deploy"
  role   = aws_iam_role.deploy["assets"].id
  policy = data.aws_iam_policy_document.assets_deploy.json
}

data "aws_iam_policy_document" "frontend_deploy" {
  statement {
    sid = "CreateFrontendBucket"

    actions = [
      "s3:CreateBucket",
      "s3:ListAllMyBuckets"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ManageFrontendBuckets"

    actions = [
      "s3:*"
    ]

    resources = [
      "arn:aws:s3:::ctbus-site-frontend-*",
      "arn:aws:s3:::ctbus-site-frontend-*/*"
    ]
  }

  statement {
    sid = "ManageFrontendCloudFront"

    actions = [
      "cloudfront:CreateCloudFrontOriginAccessIdentity",
      "cloudfront:CreateDistribution",
      "cloudfront:CreateFunction",
      "cloudfront:DeleteCloudFrontOriginAccessIdentity",
      "cloudfront:DeleteDistribution",
      "cloudfront:DeleteFunction",
      "cloudfront:DescribeFunction",
      "cloudfront:GetCloudFrontOriginAccessIdentity",
      "cloudfront:GetCloudFrontOriginAccessIdentityConfig",
      "cloudfront:GetDistribution",
      "cloudfront:GetDistributionConfig",
      "cloudfront:GetFunction",
      "cloudfront:GetFunctionConfig",
      "cloudfront:ListTagsForResource",
      "cloudfront:PublishFunction",
      "cloudfront:TagResource",
      "cloudfront:UntagResource",
      "cloudfront:UpdateCloudFrontOriginAccessIdentity",
      "cloudfront:UpdateDistribution",
      "cloudfront:UpdateFunction"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ListFrontendHostedZone"

    actions = [
      "route53:ListHostedZonesByName"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ManageFrontendDNS"

    actions = [
      "route53:ChangeResourceRecordSets",
      "route53:GetHostedZone",
      "route53:ListResourceRecordSets"
    ]

    resources = ["arn:aws:route53:::hostedzone/*"]
  }
}

resource "aws_iam_role_policy" "frontend_deploy" {
  name   = "frontend-deploy"
  role   = aws_iam_role.deploy["frontend"].id
  policy = data.aws_iam_policy_document.frontend_deploy.json
}

data "aws_iam_policy_document" "jupyter_deploy" {
  statement {
    sid = "CreateJupyterBucket"

    actions = [
      "s3:CreateBucket",
      "s3:ListAllMyBuckets"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ManageJupyterBucket"

    actions = [
      "s3:*"
    ]

    resources = [
      "arn:aws:s3:::ctbus-site-jupyter",
      "arn:aws:s3:::ctbus-site-jupyter/*"
    ]
  }

  statement {
    sid = "ManageJupyterCloudFront"

    actions = [
      "cloudfront:CreateCloudFrontOriginAccessIdentity",
      "cloudfront:CreateDistribution",
      "cloudfront:DeleteCloudFrontOriginAccessIdentity",
      "cloudfront:DeleteDistribution",
      "cloudfront:GetCloudFrontOriginAccessIdentity",
      "cloudfront:GetCloudFrontOriginAccessIdentityConfig",
      "cloudfront:GetDistribution",
      "cloudfront:GetDistributionConfig",
      "cloudfront:ListTagsForResource",
      "cloudfront:TagResource",
      "cloudfront:UntagResource",
      "cloudfront:UpdateCloudFrontOriginAccessIdentity",
      "cloudfront:UpdateDistribution"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ListJupyterHostedZone"

    actions = [
      "route53:ListHostedZonesByName"
    ]

    resources = ["*"]
  }

  statement {
    sid = "ManageJupyterDNS"

    actions = [
      "route53:ChangeResourceRecordSets",
      "route53:GetHostedZone",
      "route53:ListResourceRecordSets"
    ]

    resources = ["arn:aws:route53:::hostedzone/*"]
  }
}

resource "aws_iam_role_policy" "jupyter_deploy" {
  name   = "jupyter-deploy"
  role   = aws_iam_role.deploy["jupyter"].id
  policy = data.aws_iam_policy_document.jupyter_deploy.json
}

data "aws_iam_policy_document" "maintenance_deploy" {
  statement {
    sid = "ManageMaintenanceLambda"

    actions = [
      "lambda:AddPermission",
      "lambda:CreateFunction",
      "lambda:CreateFunctionUrlConfig",
      "lambda:DeleteFunction",
      "lambda:DeleteFunctionUrlConfig",
      "lambda:GetFunction",
      "lambda:GetFunctionConfiguration",
      "lambda:GetFunctionUrlConfig",
      "lambda:GetPolicy",
      "lambda:ListTags",
      "lambda:TagResource",
      "lambda:UntagResource",
      "lambda:UpdateFunctionCode",
      "lambda:UpdateFunctionConfiguration",
      "lambda:UpdateFunctionUrlConfig",
      "lambda:RemovePermission"
    ]

    resources = ["arn:aws:lambda:${var.region}:*:function:maintenance"]
  }

  statement {
    sid = "PassMaintenanceRole"

    actions = [
      "iam:PassRole"
    ]

    resources = ["arn:aws:iam::*:role/maintenance-role"]
  }

  statement {
    sid = "ManageMaintenanceRole"

    actions = [
      "iam:AttachRolePolicy",
      "iam:CreateRole",
      "iam:DeleteRole",
      "iam:DetachRolePolicy",
      "iam:GetRole",
      "iam:ListAttachedRolePolicies",
      "iam:TagRole",
      "iam:UntagRole",
      "iam:UpdateAssumeRolePolicy"
    ]

    resources = ["arn:aws:iam::*:role/maintenance-role"]
  }
}

resource "aws_iam_role_policy" "maintenance_deploy" {
  name   = "maintenance-deploy"
  role   = aws_iam_role.deploy["maintenance"].id
  policy = data.aws_iam_policy_document.maintenance_deploy.json
}

data "aws_iam_policy_document" "spotify_deploy" {
  statement {
    sid = "ManageSpotifyLambda"

    actions = [
      "lambda:AddPermission",
      "lambda:CreateFunction",
      "lambda:CreateFunctionUrlConfig",
      "lambda:DeleteFunction",
      "lambda:DeleteFunctionUrlConfig",
      "lambda:GetFunction",
      "lambda:GetFunctionConfiguration",
      "lambda:GetFunctionUrlConfig",
      "lambda:GetPolicy",
      "lambda:ListTags",
      "lambda:TagResource",
      "lambda:UntagResource",
      "lambda:UpdateFunctionCode",
      "lambda:UpdateFunctionConfiguration",
      "lambda:UpdateFunctionUrlConfig",
      "lambda:RemovePermission"
    ]

    resources = ["arn:aws:lambda:${var.region}:*:function:spotify-playlists"]
  }

  statement {
    sid = "PassSpotifyRole"

    actions = [
      "iam:PassRole"
    ]

    resources = ["arn:aws:iam::*:role/spotify-playlists-role"]
  }

  statement {
    sid = "ManageSpotifyRole"

    actions = [
      "iam:AttachRolePolicy",
      "iam:CreateRole",
      "iam:DeleteRole",
      "iam:DetachRolePolicy",
      "iam:GetRole",
      "iam:ListAttachedRolePolicies",
      "iam:TagRole",
      "iam:UntagRole",
      "iam:UpdateAssumeRolePolicy"
    ]

    resources = ["arn:aws:iam::*:role/spotify-playlists-role"]
  }
}

resource "aws_iam_role_policy" "spotify_deploy" {
  name   = "spotify-deploy"
  role   = aws_iam_role.deploy["spotify"].id
  policy = data.aws_iam_policy_document.spotify_deploy.json
}

output "role_arns" {
  description = "Map of service identifiers to IAM role ARNs"
  value       = { for key, role in aws_iam_role.deploy : key => role.arn }
}
