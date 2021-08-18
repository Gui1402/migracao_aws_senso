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