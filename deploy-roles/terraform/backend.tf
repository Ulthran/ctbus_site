terraform {
  backend "s3" {
    bucket       = "ctbus-tfstates"
    key          = "ctbus_site/deploy-roles.tfstate"
    region       = "us-east-1"
    use_lockfile = true
    encrypt      = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
