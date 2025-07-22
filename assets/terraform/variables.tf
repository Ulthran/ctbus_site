variable "bucket_name" {
  type        = string
  description = "Name of S3 bucket for assets"
  default     = "ctbus-site-assets"
}

variable "hostname" {
  type        = string
  description = "Domain name for assets CDN"
  default     = "assets.charliebushman.com"
}

variable "zone_name" {
  type        = string
  description = "Route53 hosted zone"
  default     = "charliebushman.com"
}
