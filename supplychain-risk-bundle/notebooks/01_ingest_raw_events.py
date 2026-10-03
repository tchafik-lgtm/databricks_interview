from pyspark.sql import functions as F
df = spark.read.csv("./data/sample_events.csv", header=True, inferSchema=True)
df.write.mode("append").saveAsTable("sc_raw_events")
