from pyspark.sql import DataFrame, SparkSession
from pathlib import Path


def load_csv(spark: SparkSession, file_path: str, header: bool = True, delimiter: str = ",") -> DataFrame:
    if not Path(file_path).exists():
            raise FileNotFoundError(f"File not found: {file_path}")

    return spark.read.option("header", header).option("delimiter", delimiter).csv(file_path)

def write_csv(df: DataFrame, output_path: str, filename: str, one_partition: bool = False) -> None:
    if one_partition:
        df = df.coalesce(1)

    df.write.option("header", True).mode("overwrite").csv(f"{output_path}/{filename}")
