import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark_session():
    """Fixture to create a SparkSession for the unit tests."""
    spark = SparkSession.builder \
        .appName("PySpark-Test") \
        .master("local[*]") \
        .config("spark.sql.shuffle.partitions", "1") \
        .config("spark.default.parallelism", "1") \
        .getOrCreate()

    yield spark

    # Clean after tests
    spark.stop()


"""
@pytest.fixture
def sample_data_path():
    return "tests/resources/sample_data.csv"
"""


@pytest.fixture
def disable_writes(monkeypatch):
    """Disable writing during tests"""
    def mock_write(*args, **kwargs):
        pass  # do nothing

    # Patch the write method of the DataFrame
    monkeypatch.setattr("pyspark.sql.DataFrameWriter.csv", mock_write)
