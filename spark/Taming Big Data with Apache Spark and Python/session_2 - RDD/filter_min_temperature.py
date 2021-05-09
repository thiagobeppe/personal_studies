from pyspark import SparkConf, SparkContext

path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/1800.csv'
conf = SparkConf().setMaster('local').setAppName("FilterMinTemperature")
sc = SparkContext.getOrCreate(conf=conf)

def parseLines(line):
    fields = line.split(",")
    stations = fields[0]
    type_of_value = fields[2]
    temp = float(fields[3]) *0.1 * (9.0/5.0) + 32.0
    return (stations,type_of_value,temp)


lines = sc.textFile(path)
parsedLines = lines.map(parseLines)
minTemps = parsedLines.filter(lambda x: "TMIN" in x[1])
tempsByStations = minTemps.map(lambda x: (x[0],x[2]))
minTempByStations = tempsByStations.reduceByKey(lambda x,y: min(x,y))

results = minTempByStations.collect()
for r in results:
    print("Station: %s\n Min Temp: %.2f Fº" % (r[0], r[1]))