variable "bucket_name" {
  type        = string
  description = "The name of the S3 bucket to host the frontend site."
  default     = "ctbus-site-frontend"
}


variable "hostname" {
  type        = string
  description = "Fully qualified domain that will point to the CloudFront distribution"
}

variable "zone_name" {
  type        = string
  description = "Route53 hosted zone to create the record in"
  default     = "charliebushman.com"
}
variable "spotify_client_id" {
  type        = string
  description = "Spotify API client ID"
}

variable "spotify_client_secret" {
  type        = string
  description = "Spotify API client secret"
}
