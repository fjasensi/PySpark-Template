class SparkSessionSingleton:
    _instance = None
    _spark = None

    def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super(SparkSessionSingleton, cls).__new__(cls)
            return cls._instance

    def __init__(self, app_name="DefaultApp", configs=None):
        if self._spark is None:
            from pyspark.sql import SparkSession

            builder = SparkSession.builder.appName(app_name)

            if configs:
                for key, value in configs.items():
                    builder = builder.config(key, value)

            self._spark = builder.getOrCreate()

    @property
    def session(self):
        if self._spark is None:
            raise RuntimeError("SparkSession is not initialized")
        return self._spark

    def stop(self):
        if self._spark is not None:
            self._spark.stop()
            self._spark = None
