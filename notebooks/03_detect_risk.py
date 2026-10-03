from pyspark.sql import functions as F
df = spark.table("sc_orders_enriched")
df = df.withColumn("is_at_risk", F.col("region") == "NA")
df.write.mode("overwrite").saveAsTable("sc_orders_risk")
