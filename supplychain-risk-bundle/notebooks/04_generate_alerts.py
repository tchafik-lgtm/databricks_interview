from pyspark.sql import functions as F
df = spark.table("sc_orders_risk")
alerts = df.filter("is_at_risk = true").withColumn("owner", F.lit(None))
alerts.write.mode("overwrite").saveAsTable("sc_orders_alerts")
