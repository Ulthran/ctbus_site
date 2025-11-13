<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
import CodeBlock from "../components/CodeBlock.vue";
const posts = window.posts;
const slug = "terraform-monolith-to-microservice";
const info = posts[slug];

const api_migrate = `
#!/bin/bash

STATE_IN="/home/ctbus/minecraft/backup.tfstate"
STATE_OUT="/home/ctbus/minecraft/services/tenant_api/terraform.tfstate"

echo "⏳ Starting migration of tenant_api module..."

# IAM
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" module.tenant_api.aws_iam_role.lambda aws_iam_role.lambda
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" module.tenant_api.aws_iam_role_policy.tenant_permissions aws_iam_role_policy.tenant_permissions
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" module.tenant_api.aws_iam_role_policy_attachment.lambda_logs aws_iam_role_policy_attachment.lambda_logs

# DynamoDB
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" module.tenant_api.aws_dynamodb_table.server_registry aws_dynamodb_table.server_registry
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" module.tenant_api.aws_dynamodb_table.interest_list aws_dynamodb_table.interest_list

# Archive data sources
for fn in server_status cost_report init_server build_status delete_stack resource_metrics ec2_metrics interest_signup create_checkout_session; do
  terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
    module.tenant_api.data.archive_file.$fn \
    data.archive_file.$fn
done

# Lambda functions
for fn in server_status cost_report init_server build_status delete_stack resource_metrics ec2_metrics interest_signup create_checkout_session; do
  terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
    module.tenant_api.aws_lambda_function.$fn \
    aws_lambda_function.$fn
done

# Lambda permissions
for perm in apigw_status apigw_cost apigw_init apigw_build_status apigw_checkout apigw_delete apigw_metrics apigw_ec2_metrics apigw_interest; do
  terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
    module.tenant_api.aws_lambda_permission.$perm \
    aws_lambda_permission.$perm
done

# API Gateway: API, Authorizer
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" module.tenant_api.aws_apigatewayv2_api.this aws_apigatewayv2_api.this
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" module.tenant_api.aws_apigatewayv2_authorizer.jwt aws_apigatewayv2_authorizer.jwt

# API Gateway: Integrations
for int in build_status checkout cost delete ec2_metrics init interest metrics status; do
  terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
    module.tenant_api.aws_apigatewayv2_integration.$int \
    aws_apigatewayv2_integration.$int
done

# API Gateway: Routes
for route in build_status checkout cost delete ec2_metrics init interest metrics status; do
  terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
    module.tenant_api.aws_apigatewayv2_route.$route \
    aws_apigatewayv2_route.$route
done

# API Gateway: Stage
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" module.tenant_api.aws_apigatewayv2_stage.prod aws_apigatewayv2_stage.prod

echo "✅ Migration complete. Listing migrated resources:"
terraform state list -state="$STATE_OUT"
`;

const frontend_migrate = `
#!/bin/bash

STATE_IN="/home/ctbus/minecraft/backup.tfstate"
STATE_OUT="/home/ctbus/minecraft/services/frontend_site/terraform.tfstate"

echo "⏳ Starting migration of frontend_site module..."

# Bucket
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.aws_s3_bucket.this \
  aws_s3_bucket.this

# Bucket policy
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.aws_s3_bucket_policy.allow_cloudfront \
  aws_s3_bucket_policy.allow_cloudfront

# CloudFront OAI
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.aws_cloudfront_origin_access_identity.this \
  aws_cloudfront_origin_access_identity.this

# CloudFront Function
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.aws_cloudfront_function.spa_rewrite \
  aws_cloudfront_function.spa_rewrite

# CloudFront Distribution
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.aws_cloudfront_distribution.this \
  aws_cloudfront_distribution.this

# Route53 zone data source
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.data.aws_route53_zone.selected \
  data.aws_route53_zone.selected

# Route53 records
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.aws_route53_record.root_alias \
  aws_route53_record.root_alias

terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.aws_route53_record.www_alias \
  aws_route53_record.www_alias

# IAM policy doc
terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" \
  module.frontend_site.data.aws_iam_policy_document.allow_cloudfront \
  data.aws_iam_policy_document.allow_cloudfront

# All static site assets
terraform state list -state="$STATE_IN" | grep 'aws_s3_object.site' | while read -r line; do
  terraform state mv -backup=- -state="$STATE_IN" -state-out="$STATE_OUT" "$line" "$line"
done

echo "✅ Migration complete. Listing migrated resources:"
terraform state list -state="$STATE_OUT"
`;
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :mod_date="info.mod_date"
    :tags="info.tags"
    :img="`ASSETS_BASE_URL/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <SectionTitle>Intro</SectionTitle>
    <Paragraph>
      This post will outline the process of migrating Terraform resources from a
      single monolithic configuration to a microservice-oriented structure. From
      monolith to microservice, follow these steps per service: - Remove
      `backend.tf` - Run `terraform init` - Move state for each resource from
      backup file to service e.g. `terraform state mv
      -state=/home/ctbus/minecraft/backup.tfstate -state-out=terraform.tfstate
      module.account.aws_organizations_account.tenants
      aws_organizations_account.tenants` - Check success with `terraform state
      list` - Create and fill in `terraform.tfvars` - Run `terraform apply` to
      create outputs (and verify there are no infrastructure changes) - Run `git
      restore backend.tf` - Run `terraform init -migrate-state`
    </Paragraph>

    <SectionTitle>API Migration</SectionTitle>

    <CodeBlock
      :code="api_migrate"
      language="bash"
      title="tenant_api/migrate.sh"
    />

    <SectionTitle>Frontend Migration</SectionTitle>

    <CodeBlock
      :code="frontend_migrate"
      language="bash"
      title="frontend/migrate.sh"
    />
  </v-container>
</template>
