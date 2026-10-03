from pyspark.sql import functions as F
alerts = spark.table("sc_orders_alerts")
rem = alerts.withColumn("action", F.lit("Email carrier"))
rem.write.mode("overwrite").saveAsTable("sc_orders_remediation")
