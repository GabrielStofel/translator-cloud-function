provider "google" {
  project = local.project_id
  region  = local.region
}

locals {
  project_id           = "gcp-sandbox-gss"
  region               = "us-east1"
  function_bucket      = "gcp-sandbox-gss-functions"
  function_name        = "translator-function"
  function_description = "This function translates a received text to a specified targeted language"
}

data "archive_file" "function_zip" {
  type        = "zip"
  source_dir  = "../src/"
  output_path = "tmp/function_archive.zip"
}

resource "google_storage_bucket_object" "object" {
  bucket = local.function_bucket
  name   = "translator-function-${data.archive_file.function_zip.output_md5}"
  source = data.archive_file.function_zip.output_path
}

resource "google_cloudfunctions_function" "function" {
  name        = local.function_name
  description = local.function_description
  runtime     = "python39"

  entry_point           = "run"
  trigger_http          = true
  ingress_settings      = "ALLOW_INTERNAL_ONLY"
  source_archive_bucket = local.function_bucket
  source_archive_object = google_storage_bucket_object.object.name
}