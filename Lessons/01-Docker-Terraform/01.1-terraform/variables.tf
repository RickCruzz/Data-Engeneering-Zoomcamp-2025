variable "project" {
  description = "Project ID"
  default     = "zoomcamp-2025-451318"
}

variable "region" {
  description = "Region of The Project"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "BigQuery Dataset Name"
  default     = "ny_taxis_zoomcamp_2025"
}

variable "gcs_bucket_name" {
  description = "Bucket Name"
  default     = "ny-taxis-bucket-zoomcamp-2025"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

