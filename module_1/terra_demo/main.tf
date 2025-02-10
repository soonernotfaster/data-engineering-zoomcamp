variable "project_id" {
  type = string
}

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.19.0"
    }
  }
}

provider "google" {
  project     = var.project_id
  region      = "useast1"
  credentials = "./keys/creds.json"
}

resource "google_storage_bucket" "example_bucket" {
  name          = "example-ssolo-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }
}
