from pyspark import SparkConf, SparkContext


path = "/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/Book.txt"
conf = SparkConf().setMaster("local").setAppName("CountingWords")
sc = SparkContext.getOrCreate(conf=conf)

rdd = sc.textFile(path)
words = rdd.flatMap(lambda x: x.split(" "))

totalWords = words.countByValue()

for word, count in totalWords.items():
    cleanWord = word.encode('ascii', 'ignore')
    if cleanWord:
        print(cleanWord, count)

