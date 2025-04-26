from src.utils.spark_session import SparkSessionSingleton


def test_singleton_instance():
    """We want only one instance of singleton."""
    singleton1 = SparkSessionSingleton(app_name="Test1")
    singleton2 = SparkSessionSingleton(app_name="Test2")

    # Verify both instances are the same instance
    assert singleton1 is singleton2

    # Verify that the configuration of the first singleton prevails
    assert singleton1.session.conf.get("spark.app.name") == "Test1"


def test_spark_session_creation():
    """Verify that the SparkSession is created correctly."""
    singleton = SparkSessionSingleton(app_name="TestApp")
    spark = singleton.session

    # Verify that the session is not None
    assert spark is not None

    # Verify that you can perform basic operations
    test_df = spark.createDataFrame([(1, "a"), (2, "b")], ["num", "letter"])
    assert test_df.count() == 2