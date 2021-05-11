from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructField, StructType, IntegerType, FloatType, StringType

spark = SparkSession.builder.appName("MinMaxTemp").getOrCreate()
path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/1800.csv'

schema = StructType([ StructField("stationID",StringType(),True), \
                      StructField("date",IntegerType(),True), \
                      StructField("measure_type",StringType(),True), \
                      StructField("temperature",FloatType(),True)])

df = spark.read.schema(schema).csv(path)

minTemps = df.filter(func.col("measure_type") == "TMIN")
maxTemps = df.filter(func.col("measure_type") == "TMAX")

stationMinTempsF = minTemps.withColumn("temperature", func.round(func.col("temperature") * 0.1 * (9.0/5.0) + 32.0,2))
stationMaxTempsF = maxTemps.withColumn("temperature", func.round(func.col("temperature") * 0.1 * (9.0/5.0) + 32.0,2))

stationMinTemps = stationMinTempsF.groupBy("stationID").min("temperature")
stationMaxTemps = stationMaxTempsF.groupBy("stationID").max("temperature")

stationMinTemps.show()
stationMaxTemps.show()

spark.stop()