from pyspark.sql import functions as func
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, LongType

path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/ml-100k/u.data'
path_movie_name = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/ml-100k/u.item'

spark = SparkSession.builder.appName("MostPopularMovies").getOrCreate()

schema = StructType([StructField ("userID",IntegerType(),True), 
                        StructField ("movieID",IntegerType(),True), 
                        StructField ("rating",IntegerType(),True), 
                        StructField ("timestamp",LongType(),True)])

def loadMovieNames():
    movieNames = {}
    with open(path_movie_name, "r", encoding="ISO-8859-1", errors="ignore") as f:
        for line in f:
            fields = line.split("|")
            movieNames[int(fields[0])] = fields[1]
    return movieNames

def lookupName(movieID):
    return nameDict.value[movieID]

lookupNameUDF = func.udf(lookupName)

nameDict = spark.sparkContext.broadcast(loadMovieNames())
moviesDF = spark.read.option("sep","\t").schema(schema).csv(path)
topMovies = moviesDF.groupBy("movieID").count().orderBy(func.desc("count"))
moviesWithName = topMovies.withColumn("movieTitle", lookupNameUDF(func.col("movieID")))

moviesWithName.show(10, False)

spark.stop()