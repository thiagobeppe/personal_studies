from pyspark.sql import SparkSession
from pyspark.sql import functions as func

spark = SparkSession.builder.appName("WordCount").getOrCreate()
path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/Book.txt'

inputDF = spark.read.text(path)

words = inputDF.select(func.explode(func.split(inputDF.value, r"\W+")).alias("word"))
words = words.filter(words.word != "")

lowerWords = words.select(func.lower(words.word).alias("word"))
wordCounts = lowerWords.groupBy("word").count()
wordCountsSorted = wordCounts.orderBy(func.col("count").desc())
wordCountsSorted.show(100, truncate = 0)