from pyspark import SparkConf, SparkContext
from operator import add
import string

input_file = "file:///usr/local/spark/input.txt"
output_file = "file:///usr/local/spark/output.txt"

conf = SparkConf().setMaster('local').setAppName('BigramCount')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile(input_file)

sentences = RDDvar.flatMap(lambda line: line.split("."))
words = sentences.flatMap(lambda line: line.split(" "))
bigrams = words.flatMap(lambda xs: zip(xs, xs[1:]))

result = bigrams.map(lambda bigram: (bigram, 1))
aggreg1 = result.reduceByKey(add)

result.saveAsTextFile(output_file)
