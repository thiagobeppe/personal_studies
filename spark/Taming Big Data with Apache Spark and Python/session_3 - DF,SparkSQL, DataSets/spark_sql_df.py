from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/fakefriends_header.csv'

people = spark.read.option("header","true").option("inferSchema","true").csv(path)

people.printSchema()

people.select("name").show()

people.filter(people.age < 21).show()

people.groupBy("age").count().show()

people.select(people.name, people.age +10).show()

spark.stop()    