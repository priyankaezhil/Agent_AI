import pandas as pd
import sqlite3
import os

# Step 1: Connect to SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Step 2: Load each CSV file
data_path = os.path.join("data")

ad_sales = pd.read_csv("data/ad_sales.csv")
eligibility = pd.read_csv("data/eligibility.csv")
total_sales = pd.read_csv("data/total_sales.csv")


# Step 3: Write each DataFrame to a table
ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)
total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)

print("✅ All CSVs loaded into ecommerce.db successfully.")

# Step 4: Close the connection
conn.close()
