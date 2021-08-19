provider "aws" {
  region = var.regiao
}


terraform {
  backend "s3" {
    bucket = "terraform-state-igti-guilherme"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }

}