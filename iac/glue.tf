resource "aws_glue_job" "transform" {
  name     = "senso_transform_parquet"
  role_arn = var.glue_role

  command {
    script_location = "s3://${aws_s3_bucket.datalake.id}/scripts/pyspark/transform.py"
    python_version  = "3"
  }

  default_arguments = {
    "--job-language" = "python"
  }
}


resource "aws_glue_trigger" "trigger_job" {
  name = "run"
  type = "ON_DEMAND"

  actions {
    job_name = aws_glue_job.transform.name
  }
}



resource "aws_glue_crawler" "senso_crowler_docentes" {
  database_name = "senso"
  name          = "senso_crowler_docentes"
  role          = "arn:aws:iam::595877458560:role/service-role/AWSGlueServiceRole-testeigti2"

  s3_target {
    path = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}/staging/senso/docentes/"

  }
}



resource "aws_glue_crawler" "senso_crowler_escolas" {
  database_name = "senso"
  name          = "senso_crowler_escolas"
  role          = "arn:aws:iam::595877458560:role/service-role/AWSGlueServiceRole-testeigti2"

  s3_target {
    path = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}/staging/senso/escolas/"

  }
}


resource "aws_glue_crawler" "senso_crowler_gestor" {
  database_name = "senso"
  name          = "senso_crowler_gestor"
  role          = "arn:aws:iam::595877458560:role/service-role/AWSGlueServiceRole-testeigti2"

  s3_target {
    path = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}/staging/senso/gestor/"

  }
}


resource "aws_glue_crawler" "senso_crowler_matricula" {
  database_name = "senso"
  name          = "senso_crowler_matricula"
  role          = "arn:aws:iam::595877458560:role/service-role/AWSGlueServiceRole-testeigti2"

  s3_target {
    path = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}/staging/senso/matricula/"

  }
}


resource "aws_glue_crawler" "senso_crowler_turmas" {
  database_name = "senso"
  name          = "senso_crowler_turmas"
  role          = "arn:aws:iam::595877458560:role/service-role/AWSGlueServiceRole-testeigti2"

  s3_target {
    path = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}/staging/senso/turmas/"

  }
}