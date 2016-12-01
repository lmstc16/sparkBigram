from pyspark import SparkConf, SparkContext
from operator import add
import string

input_file = "file:///usr/local/spark/input.txt"
output_file = "file:///usr/local/spark/output"

conf = SparkConf().setMaster('local').setAppName('BigramCount')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile(input_file)

bigrams = RDDvar.flatMap(lambda line: line.split(".")) \
                .map(lambda sentences: sentences.split(" ")) \
                .flatMap(lambda word: zip(word, word[1:])) \
                .map(lambda bigram: (bigram, 1)) \
                .reduceByKey(add) \
                .sortBy(lambda x: x[1], False)

most_common = bigrams.first()[0]

mylen = bigrams.count()

agg = bigrams.map(lambda a: (0, a[1]))
top = agg.reduce(lambda a, b: (a[0] + 1, a[1] + b[1]) if a[1] + b[1] < mylen / 10 else a)

file = open("/usr/local/spark/result.txt", "w")
file.write("the total number of bigrams: %d \n" %(mylen))
file.write("the most common bigram: %s \n" %(most_common))
file.write("the number of bigrams required to add up to 10 percent of all bigrams: %d" %(top[0]))
file.close()

bigrams.saveAsTextFile(output_file)
