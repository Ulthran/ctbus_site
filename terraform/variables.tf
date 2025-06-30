variable "bucket_name" {
  type        = string
  description = "The name of the S3 bucket to host the frontend site."
  default     = "ctbus-site-frontend"
}

variable "cdn_url" {
  type        = string
  description = "The URL of the assets CDN."
}