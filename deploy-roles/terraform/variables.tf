variable "region" {
  type        = string
  description = "AWS region where IAM roles will be created"
  default     = "us-east-1"
}

variable "github_owner" {
  type        = string
  description = "GitHub organization or user that owns the repository"
  default     = "charliebushman"
}

variable "repository" {
  type        = string
  description = "Repository name for which to trust GitHub Actions"
  default     = "ctbus_site"
}

variable "role_name_prefix" {
  type        = string
  description = "Prefix for IAM role names"
  default     = "ctbus"
}
