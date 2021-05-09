import re

from pyspark import SparkConf, SparkContext


path = "/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/Book.txt"
conf = SparkConf().setMaster("local").setAppName("CountingWords")
sc = SparkContext.getOrCreate(conf=conf)

def normalizeDate(txt):
    return re.compile(r'\W+', re.UNICODE).split(txt.lower())

rdd = sc.textFile(path)
words = rdd.flatMap(normalizeDate)

totalWords = words.countByValue()

for word, count in totalWords.items():
    cleanWord = word.encode('ascii', 'ignore')
    if cleanWord:
        print(cleanWord, count)