terraform {
  backend "gcs" {
    bucket  = "gcp-sandbox-gss-tfstate"
    prefix  = "translator_function"
  }
}