from pyspark import SparkConf, SparkContext


path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/fakefriends.csv'
conf = SparkConf().setMaster('local').setAppName("AvgByAge")
sc = SparkContext.getOrCreate(conf=conf)

def parseLines(line):
    fields = line.split(",")
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age,numFriends)

lines = sc.textFile(path)
rdd = lines.map(parseLines)

totalAgeByValues = rdd.mapValues(lambda x: (x,1)) \
                    .reduceByKey(lambda x,y: (x[0] + x[1], y[0]+ y[1]))

# avgByAge = totalAgeByValues.map(lambda x: (x[0], x[1][0]/x[1][1]))
avgByAge = totalAgeByValues.mapValues(lambda x: x[0]/x[1])

results = avgByAge.collect()
for r in results:
    print("Age: %i \nFriends Average: %.2f \n" % (r[0], r[1]))