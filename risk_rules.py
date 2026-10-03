from pyspark.sql import functions as F
def apply_basic_rules(df):
    return df.withColumn("is_at_risk", F.lit(True))
