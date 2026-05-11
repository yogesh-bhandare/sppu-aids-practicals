import pandas as pd
from sqlalchemy import create_engine

# pymysql
engine = create_engine("mysql+pymysql://root:@localhost:3306/retail_management")
# engine = create_engine("mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/retail_management")
db_data = pd.read_sql("SELECT * FROM home_product", engine)

csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
csv_data = pd.read_csv(csv_url)

print("Database Data")
print(db_data.head())

print("\nCSV Data")
print(csv_data.head())

combined_data = pd.concat([db_data, csv_data], ignore_index=True)

combined_data = combined_data.drop_duplicates()

print("\nTransformed Data")
print(combined_data.head())

combined_data.to_sql(
    name="integrated_data", con=engine, if_exists="replace", index=False
)

print("Data successfully integrated and loaded into MySQL database")
