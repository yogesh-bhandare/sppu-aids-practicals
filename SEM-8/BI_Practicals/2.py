import pandas as pd
from sqlalchemy import create_engine

dataset_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

data = pd.read_csv(dataset_url)

print("Extracted Data")
print(data.head())

data = data.dropna()

data = data.drop_duplicates()

data["tip_percentage"] = (data["tip"] / data["total_bill"]) * 100

data["tax_amount"] = data["total_bill"] * 0.18

data["total_with_tax"] = data["total_bill"] + data["tax_amount"]

data["bill_per_person"] = data["total_bill"] / data["size"]

data["tip_per_person"] = data["tip"] / data["size"]

data["tip_category"] = pd.cut(
    data["tip_percentage"], bins=[0, 10, 20, 100], labels=["Low", "Medium", "High"]
)

print("\nTransformed Data")
print(data.head())

engine = create_engine("mysql+pymysql://root:@localhost:3306/etl_db")

data.to_sql(name="tips_analysis", con=engine, if_exists="replace", index=False)

print("ETL Process Completed and Data Loaded into MySQL")
