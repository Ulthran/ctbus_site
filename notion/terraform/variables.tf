variable "notion_token" {
  type        = string
  description = "Notion internal integration token"
  sensitive   = true
}

variable "notion_automations_db_id" {
  type        = string
  description = "Notion Automations database ID"
}

variable "notion_tasks_db_id" {
  type        = string
  description = "Notion Tasks database ID"
  default     = "647c5b7e-4759-4886-9e79-4877d83b0a1d"
}
