terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.20.0"
    }
  }
}

provider "google" {
  # Configuration options
  project   =   "zoomcamp-2025"
  region    =   "us-central1"
}