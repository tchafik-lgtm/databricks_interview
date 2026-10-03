risk_df = spark.table("sc_orders_risk")
alerts_df = spark.table("sc_orders_alerts")
display(risk_df)
display(alerts_df)
