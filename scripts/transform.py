import sys
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

raw_dir = "s3://datalake-bootcamp-igti-prod-595877458560/raw-data/senso/"
staging_dir = "s3://datalake-bootcamp-igti-prod-595877458560/staging/senso/"


## Carregando dados 

docentes_co = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "docentes_co/")
    
)

docentes_nordeste = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "docentes_nordeste/")
    
)

docentes_norte = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "docentes_norte/")
    
)


docentes_sudeste = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "docentes_sudeste/")
    
)


docentes_sul = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "docentes_sul/")
    
)



matricula_co = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "matricula_co/")
    
)

matricula_nordeste = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "matricula_nordeste/")
    
)

matricula_norte = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "matricula_norte/")
    
)


matricula_sudeste = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "matricula_sudeste/")
    
)


matricula_sul = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "matricula_sul/")
    
)



escolas = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "escolas/")
    
)



gestor = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "gestor/")
    
)


turmas = (
    
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load(raw_dir + "turmas/")
    
)

docentes = (
    docentes_co
    .unionAll(docentes_nordeste)
    .unionAll(docentes_norte)
    .unionAll(docentes_sudeste)
    .unionAll(docentes_sul)
)



matricula = (
    matricula_co
    .unionAll(matricula_nordeste)
    .unionAll(matricula_norte)
    .unionAll(matricula_sudeste)
    .unionAll(matricula_sul)
)



## Save data

(
    
    docentes
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save(staging_dir + 'docentes')

)

(
    
    matricula
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save(staging_dir + 'matricula')

)


(
    
    turmas
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save(staging_dir + 'turmas')

)


(
    
    gestor
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save(staging_dir + 'gestor')

)

(
    
    escolas
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save(staging_dir + 'escolas')

)