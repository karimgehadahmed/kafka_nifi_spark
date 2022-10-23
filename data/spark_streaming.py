from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,FloatType,IntegerType,StringType
from pyspark.sql.functions import from_json,col
from datetime import datetime
import uuid
movieSchema = StructType([
                StructField("movie_name",StringType(),True),
                StructField("language",StringType(),True),
                StructField("imdb_rating",IntegerType(),True),
                StructField("run_time",StringType(),True),
                StructField("year",IntegerType(),True),
                StructField("maturity",StringType(),True),
                StructField("plot",StringType(),True),
            ])
spark = SparkSession \
    .builder \
    .appName("SparkStructuredStreaming") \
    .config("spark.driver.host", "localhost")\
    .getOrCreate()



spark.sparkContext.setLogLevel("ERROR")



df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "172.18.0.4:9092") \
  .option("subscribe", "amazonprime") \
  .option("delimeter",",") \
  .option("startingOffsets", "earliest") \
  .load() 

df.printSchema()

df1 = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"),movieSchema).alias("data")).select("data.*")
df2 = df1.selectExpr("current_timestamp() as date_time","AVG(imdb_rating) as average_rating","count(*) as total_count","max(imdb_rating) as max_rating" , "min(imdb_rating) as min_rating")

df1.printSchema()
df2.printSchema()
# # df_p = df1.to_pandas()
# # df_p['time_stamp']=datetime.now()


def writeToPostGres(writeDF, _):
  writeDF.write \
    .format("jdbc")\
    .option("url", "jdbc:postgresql://172.18.0.5:5432/postgres")\
    .option("driver", "org.postgresql.Driver") \
    .option("user", "postgres").option("password", "postgres")\
    .options(dbtable="analysis_data")\
    .mode('append')\
    .save()

df2.writeStream \
    .foreachBatch(writeToPostGres) \
    .outputMode("complete") \
    .start()\
    .awaitTermination()
df2.show()