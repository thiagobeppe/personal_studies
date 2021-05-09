import collections

from pyspark import SparkConf, SparkContext

path = r"/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/ml-100k/u.data"

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext.getOrCreate(conf = conf)

lines = sc.textFile(path)
ratings = lines.map(lambda x: x.split()[2])
results = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(results.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))