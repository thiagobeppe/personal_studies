from pyspark.sql import functions as func
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StructType, IntegerType

path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/marvel-graph.txt'
path_with_names = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/marvel-names.txt'

spark = SparkSession.builder.appName("MostPopularSuperHero").getOrCreate()

schema = StructType([ StructField("id",IntegerType(),True),StructField("name",StringType(),True)])

names = spark.read.schema(schema).option("sep"," ").csv(path_with_names)
lines = spark.read.text(path)

conn = lines.withColumn("id", func.split(func.col("value"), " ")[0]) \
                .withColumn("conn", func.size(func.split(func.col("value"), " ")) -1) \
                    .groupBy("id").agg(func.sum("conn").alias("conn"))

mostPopularSH = conn.sort(func.col("conn").desc()).first()
mostPopularWithName = names.filter(func.col("id") == mostPopularSH[0]).select("name").first()

mostObscureSH = conn.sort(func.col("conn").asc()).first()
mostObscureWithName = names.filter(func.col("id") == mostObscureSH[0]).select("name").first()


print("%s is the most popular superhero with %s co-appearances" %(mostPopularWithName[0],str(mostPopularSH[1])))
print("%s is the most obscure superhero with %s co-appearances" %(mostObscureWithName[0],str(mostObscureSH[1])))