from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import LongType, StructField, StructType, IntegerType, FloatType, StringType

spark = SparkSession.builder.appName("MinMaxTemp").getOrCreate()
path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/customer-orders.csv'

schema = StructType ( [ StructField("customer_id",IntegerType(),True), 
                        StructField("timestamp", LongType(),True),
                        StructField("amount_spent",FloatType(),True)])

df = spark.read.schema(schema).csv(path)

groupedDf = df.groupBy(func.col("customer_id")).sum("amount_spent").orderBy(func.col("sum(amount_spent)").desc())

results = groupedDf.collect()

for r in results:
    print("Customer ID : %s\nAmount Spent: %.2f" %(r[0],r[1]))


#Second Form
groupedDf_2 = df.groupBy(func.col("customer_id")).agg(func.round(func.sum("amount_spent"),2).alias("total_spent")).orderBy(func.col("total_spent    ").desc())
groupedDf_2.show()

spark.stop()