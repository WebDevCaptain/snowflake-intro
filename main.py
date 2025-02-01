import os
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

SNOWFLAKE_USER = os.environ.get("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.environ.get("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.environ.get("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.environ.get("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.environ.get("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.environ.get("SNOWFLAKE_SCHEMA")

# connection
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
)

# Check connection
cursor = conn.cursor()
cursor.execute("SELECT CURRENT_VERSION()")
version = cursor.fetchone()
print(f"Connected to Snowflake. Version: {version[0]}")


# Create a table
cursor.execute(
    """
    CREATE OR REPLACE TABLE customers (
        id INTEGER PRIMARY KEY,
        name STRING,
        email STRING,
        age INTEGER,
        city STRING
    )
"""
)

print("Table 'customers' created successfully.")
cursor.close()

cursor = conn.cursor()

# Read CSV
df = pd.read_csv("customers.csv")

# Insert data into Snowflake
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO customers (id, name, email, age, city) VALUES (%s, %s, %s, %s, %s)",
        (row["id"], row["name"], row["email"], row["age"], row["city"]),
    )

print("Data inserted into Snowflake successfully.")

cursor.close()


# Querying data
cursor = conn.cursor()
cursor.execute("SELECT * FROM customers LIMIT 5")

for row in cursor.fetchall():
    print(row)

cursor.close()


# Analytics
cursor = conn.cursor()
cursor.execute("SELECT AVG(age) FROM customers")
print(f"Average age: {cursor.fetchone()[0]}")
cursor.close()


# Reading data from Snowflake
df = pd.read_sql("SELECT * FROM customers", conn)
print(df.head())


conn.close()
