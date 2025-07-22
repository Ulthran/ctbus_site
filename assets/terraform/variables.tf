variable "bucket_name" {
  type        = string
  description = "Name of S3 bucket for assets"
  default     = "ctbus-site-assets"
}

variable "hostname" {
  type        = string
  description = "Domain name for assets CDN"
}

variable "additional_aliases" {
  type        = list(string)
  description = "Additional DNS names for the assets CDN"
  default     = []
}

variable "zone_name" {
  type        = string
  description = "Route53 hosted zone"
  default     = "charliebushman.com"
}
