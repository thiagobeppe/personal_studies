from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/fakefriends_header.csv'

people = spark.read.option("header","true").option("inferSchema","true").csv(path)

#Using SQL
people.createOrReplaceTempView("people")
results_sql = spark.sql("SELECT age, AVG(numFriends) as average_num_friends FROM people GROUP BY age ORDER BY 1")

for r in results_sql.collect():
    print(r)

#Using native functions
people.select("age","numFriends").groupBy("age").avg("numFriends").orderBy(people.age).show(100)

spark.stop()