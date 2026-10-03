from pyspark.sql import functions as F
orders = spark.read.csv("./data/sample_orders.csv", header=True, inferSchema=True)
orders = orders.withColumn("carrier", F.lit("UNKNOWN"))
orders.write.mode("overwrite").saveAsTable("sc_orders_enriched")
