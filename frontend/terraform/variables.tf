variable "bucket_name" {
  type        = string
  description = "Name of the S3 bucket to host the frontend"
  default     = "ctbus-site-frontend"
}

variable "hostname" {
  type        = string
  description = "Domain name for the frontend"
}

variable "additional_aliases" {
  type        = list(string)
  description = "Additional DNS names"
  default     = []
}

variable "zone_name" {
  type        = string
  description = "Route53 hosted zone"
  default     = "charliebushman.com"
}
