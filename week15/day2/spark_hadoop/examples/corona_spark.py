"""
python3.6 -m pip install pyspark

# Dataframe tutorial
https://www.guru99.com/pyspark-tutorial.html#3

#Tensorflow on spark training model: 
https://www.adaltas.com/en/2018/05/29/spark-tensorflow-2-3/

"""

import findspark
findspark.init()

# PySpark
import pyspark
from pyspark import SparkFiles
from pyspark import SparkContext, SparkConf

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import SQLContext
from pyspark.sql import functions as F

import time

LOCAL_FILE = "/home/consciencesai/consciencesai/data_science_developer/projects_source/pyspark_python/data/corona_full_data.csv"

# Spark config
conf = SparkConf().setAppName('CoronaSpark')
sc = SparkContext(conf=conf)
sc.addFile(LOCAL_FILE)  

# Create a spark session
spark = SparkSession.builder.getOrCreate()

# Create pandas data frame and convert it to a spark data frame 
spark_file = SparkFiles.get("corona_full_data.csv")

df = spark.read.load(spark_file,
                     format="csv", inferSchema="true", header="true")
#df.set_index("date")

df.printSchema()
df.show(5, truncate = False)

df_spain = df[df.location == "Spain"]

df_spain.printSchema()
df_spain.show(5, truncate = False)

start_time = time.time()

df_spain.select()

count = 0
while count != 2000:
    sql_result = df_spain.take(count)
    first_result = sql_result[0] if len(sql_result) > 0 else ["First", "Second"]
    print(first_result)
    print(type(first_result))
    print(first_result[0])
    print(first_result[1])
    print("*********************")
    count += 1

print("--- %s seconds ---" % (time.time() - start_time))