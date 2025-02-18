terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.20.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = "./keys/credentials.json"
  project     = "zoomcamp-2025-451318"
  region      = "us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "demo-bucket-zoomcamp-2025"
  location      = "US"
  force_destroy = true

}