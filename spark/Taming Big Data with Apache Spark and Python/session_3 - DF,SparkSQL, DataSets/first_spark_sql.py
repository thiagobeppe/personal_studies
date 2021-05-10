from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/fakefriends.csv'

def mapper(line):
    fields = line.split(",")
    return Row(ID =int(fields[0]), name = str(fields[1]), 
                    age= int(fields[2]),numFriends = int(fields[3]))

lines = spark.sparkContext.textFile(path)
people = lines.map(mapper)

schemaPeople = spark.createDataFrame(people).cache()
schemaPeople.createOrReplaceTempView("people")

teenagers = spark.sql("SELECT * FROM people WHERE age >=13 and age <=19")
for teen in teenagers.collect():
    print(teen)

schemaPeople.groupBy("age").count().orderBy("age").show()

spark.stop()