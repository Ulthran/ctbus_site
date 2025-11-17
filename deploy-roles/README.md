# Deployment IAM roles

This Terraform project provisions the IAM roles that our GitHub Actions
workflows assume to run `terraform apply` for each service. There is no CI/CD
pipeline for this project; apply changes manually whenever new roles or
permissions are required.

The configuration creates a GitHub OIDC provider and one role per service. By
default the roles trust workflows from the `charliebushman/ctbus_site`
repository that run on the `master` or `main` branches. Update the variables
in [`variables.tf`](terraform/variables.tf) if you need to change the defaults.

## Role permissions

Each role grants only the AWS permissions required by its corresponding
Terraform project:

- **assets** – manages the `ctbus-site-assets` S3 bucket and objects, the
  CloudFront distribution and origin access identity that front the bucket, and
  the Route 53 records for `charliebushman.com`.
- **frontend** – manages the `ctbus-site-frontend-*` S3 buckets (one per
  workspace), the SPA rewrite CloudFront Function, the CloudFront distribution,
  and the Route 53 aliases that point at the distribution.
- **jupyter** – manages the `ctbus-site-jupyter` S3 bucket and objects, the
  CloudFront distribution/origin access identity, and the associated Route 53
  DNS alias.
- **maintenance** – creates and updates the `maintenance` Lambda function,
  public function URL, and the dedicated execution IAM role the function uses.
- **spotify** – creates and updates the `spotify-playlists` Lambda function,
  its public function URL, and the execution IAM role the Lambda assumes.

## Usage

```sh
cd terraform
terraform init
terraform plan
terraform apply
```
