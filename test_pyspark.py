from pyspark.sql import SparkSession
import findspark


# Create a Spark session

findspark.init()
spark = SparkSession.builder \
    .master("local") \
    .appName("PySparkTest") \
    .getOrCreate()

# Create a simple DataFrame
data = [("Alice", 25), ("Bob", 30), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()