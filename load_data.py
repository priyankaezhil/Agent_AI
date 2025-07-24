import pandas as pd
import sqlite3
import os

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

data_path = os.path.join("data")

ad_sales = pd.read_csv("data/ad_sales.csv")
eligibility = pd.read_csv("data/eligibility.csv")
total_sales = pd.read_csv("data/total_sales.csv")

ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)
total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)

print("✅ All CSVs loaded into ecommerce.db successfully.")

conn.close()
