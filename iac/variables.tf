# Criacao de variaveis para facilitar a criacao e reaproveitamento de codigos em tf
variable "base_bucket_name" {
  default = "datalake-bootcamp-igti"
}

variable "ambiente" {
  default = "prod"
}

variable "numero_conta" {
  default = "595877458560"
}

variable "glue_role" {
  default = "arn:aws:iam::595877458560:role/AWSGlueServiceRole-teste-igti"
}

variable "regiao" {
  default = "us-east-2"
}