from pyspark.sql import functions as F
def generate_playbook(alerts_df):
    return alerts_df.withColumn("action", F.lit("Notify carrier"))
