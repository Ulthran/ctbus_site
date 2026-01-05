variable "bucket_name" {
  type        = string
  description = "Name of the S3 bucket to host the games site"
  default     = "ctbus-site-games"
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

variable "certificate_arn" {
  type        = string
  description = "ACM certificate ARN for CloudFront"
  default     = "arn:aws:acm:us-east-1:832242454463:certificate/f7e30d65-53f8-4852-834a-32d29ca145eb"
}
