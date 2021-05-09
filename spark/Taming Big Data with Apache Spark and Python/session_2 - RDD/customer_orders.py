from pyspark import SparkConf, SparkContext

path = '/home/tbeppe/Documents/studies/courses/spark/Taming Big Data with Apache Spark and Python/datasets/customer-orders.csv'
conf = SparkConf().setMaster('local').setAppName("AvgByAge")
sc = SparkContext.getOrCreate(conf=conf)

def parseLines(line):
    fields = line.split(',')
    fields_id = fields[0]
    amount_spent = float(fields[2])
    return (fields_id, amount_spent)

rdd = sc.textFile(path)
totalAmountSpentByID = rdd.map(parseLines).reduceByKey(lambda x,y: x+y).sortBy(lambda x: -x[1])

results = totalAmountSpentByID.collect()

for r in results:
    print("ID: %s\nAmount: %.2f" %(r[0],r[1]))