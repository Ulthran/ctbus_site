# Deployment IAM roles

This Terraform project provisions the IAM roles that our GitHub Actions
workflows assume to run `terraform apply` for each service. There is no CI/CD
pipeline for this project; apply changes manually whenever new roles or
permissions are required.

The configuration creates a GitHub OIDC provider and one role per service. By
default the roles trust workflows from the `charliebushman/ctbus_site`
repository that run on the `master` or `main` branches. Update the variables
in [`variables.tf`](terraform/variables.tf) if you need to change the defaults.

## Usage

```sh
cd terraform
terraform init
terraform plan
terraform apply
```
