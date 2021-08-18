# Criacao de recurso: "tipo" "key_terraform" 
resource "aws_s3_bucket" "datalake" {
  # Parametros de configuraçao do recurso
  bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}"
  acl    = "private"
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
  tags = {
    IES   = "IGTI"
    CURSO = "EDC"
  }


}



resource "aws_s3_bucket_object" "raw-files" {
  for_each = fileset("/home/guilherme/projetos/migracao_aws_senso/data", "*.CSV")

  bucket = aws_s3_bucket.datalake.id
  key    = "raw-data/senso/${element(split(".", "${each.value}"), 0)}/year=2020/${each.value}"
  source = "/home/guilherme/projetos/migracao_aws_senso/data/${each.value}"
  # etag makes the file update when it changes; see https://stackoverflow.com/questions/56107258/terraform-upload-file-to-s3-on-every-apply
  etag = filemd5("/home/guilherme/projetos/migracao_aws_senso/data/${each.value}")


}



resource "aws_s3_bucket_object" "scripts" {

  bucket = aws_s3_bucket.datalake.id
  key    = "scripts/pyspark/transform.py"
  acl    = "private"
  source = "../scripts/transform.py"
  etag   = filemd5("../scripts/transform.py") # so sobe o arquivo novamente se houver mudancas


}
