import pandas as pd
import numpy as np
import random
from datetime import datetime
import matplotlib.pyplot as plt


# Step 1: CREATE MANUAL DATASETS (WITH ISSUES)

np.random.seed(15)
random.seed(15)
products = ['Phone', 'Laptop', 'Tablet', 'Speaker', 'Headphone']
categories = ['Electronics', 'Computers', 'Audio']

def random_date():
    return datetime(2024, random.randint(1,6), random.randint(1,28))

#  sales.csv with missing values, duplicates, inconsistencies
csv_data = {
    'Product': [random.choice(products) for _ in range(10)] + ['Phone'],
    'Category': [random.choice(categories) for _ in range(10)] + [np.nan],
    'Sales': [random.randint(1000, 5000) for _ in range(6)] + [None, 2000, 3000, 4000, 4000],
    'OrderDate': [random_date().strftime("%d/%m/%Y") for _ in range(11)]
}
csv_df = pd.DataFrame(csv_data)
csv_df.loc[3, 'Product'] = None
csv_df.loc[5, 'Category'] = '  Electronics'
csv_df.loc[2, 'Sales'] = None
csv_df = pd.concat([csv_df, csv_df.iloc[[1]]], ignore_index=True)
csv_df.to_csv('./sales.csv', index=False)

#  sales.xlsx with different column names and duplicate row
excel_data = {
    'ProductName': [random.choice(products) for _ in range(9)] + [None],
    'Cat': [random.choice(categories) for _ in range(9)] + ['Audio'],
    'Amount': [random.randint(1500, 7000) for _ in range(5)] + [np.nan, 4000, 4000, 3000, 2500],
    'OrderDate': [random_date().strftime("%Y-%m-%d") for _ in range(10)]
}
excel_df = pd.DataFrame(excel_data)
excel_df = pd.concat([excel_df, excel_df.iloc[[0]]], ignore_index=True)
excel_df.to_excel('./sales.xlsx', index=False)

#  sales.json with inconsistencies and extra column
json_data = []
for i in range(12):
   
    cat = random.choice(categories)  
    cat_case = random.choice([cat.upper(), cat.lower()])
    row = {
        'product': random.choice([x.lower() for x in products]),
        'category': cat_case,
        'Sales': random.randint(1200, 4500) if i % 4 != 0 else None,
        'Order Date': random_date().strftime("%Y/%m/%d"),
        'Seller': random.choice(['Amit','Sara','John']) if i < 8 else None
    }
    json_data.append(row)

json_df = pd.DataFrame(json_data)
json_df = pd.concat([json_df, json_df.iloc[[2]]], ignore_index=True)
json_df.to_json('./sales.json', orient='records', lines=False)


# Step 2: LOAD DATASETS
 
csv_df = pd.read_csv('sales.csv')
excel_df = pd.read_excel('sales.xlsx')
json_df = pd.read_json('sales.json')

print("CSV\n",csv_df.head())
print("Excel\n",excel_df.head())
print("JSON\n",json_df.head())


# Step 3: CLEAN EACH DATASET INDIVIDUALLY 

#  CLEAN CSV
csv_df['Product'] = csv_df['Product'].str.strip().str.capitalize()
csv_df['Category'] = csv_df['Category'].astype(str).str.strip().str.capitalize()
csv_df['Sales'] = pd.to_numeric(csv_df['Sales'], errors='coerce')
csv_df['Product'] = csv_df['Product'].fillna('Unknown')
csv_df['Category'] = csv_df['Category'].replace('nan','Unknown').fillna('Unknown')
csv_df['Sales'] = csv_df['Sales'].fillna(csv_df['Sales'].median())
csv_df['OrderDate'] = csv_df['OrderDate'].astype(str)
csv_df = csv_df.drop_duplicates()

#  CLEAN & TRANSFORM EXCEL
excel_df = excel_df.rename(columns={'ProductName':'Product', 'Cat':'Category', 'Amount':'Sales'})
excel_df['Product'] = excel_df['Product'].str.strip().str.capitalize()
excel_df['Category'] = excel_df['Category'].astype(str).str.strip().str.capitalize()
excel_df['Sales'] = pd.to_numeric(excel_df['Sales'], errors='coerce')
excel_df['Product'] = excel_df['Product'].fillna('Unknown')
excel_df['Category'] = excel_df['Category'].replace('nan','Unknown').fillna('Unknown')
excel_df['Sales'] = excel_df['Sales'].fillna(excel_df['Sales'].median())
excel_df['OrderDate'] = excel_df['OrderDate'].astype(str)
excel_df = excel_df.drop_duplicates()

# CLEAN & TRANSFORM JSON
json_df = json_df.rename(columns={'product':'Product', 'category':'Category', 'Order Date':'OrderDate'})
json_df['Product'] = json_df['Product'].str.strip().str.capitalize()
json_df['Category'] = json_df['Category'].astype(str).str.strip().str.capitalize()
json_df['Sales'] = pd.to_numeric(json_df['Sales'], errors='coerce')
json_df['Product'] = json_df['Product'].fillna('Unknown')
json_df['Category'] = json_df['Category'].replace('nan','Unknown').fillna('Unknown')
json_df['Sales'] = json_df['Sales'].fillna(json_df['Sales'].median())
json_df['OrderDate'] = json_df['OrderDate'].astype(str)
json_df = json_df.drop(columns=['Seller'])
json_df = json_df.drop_duplicates()


def parse_order_date(date_str):
    for fmt in ["%d/%m/%Y", "%Y-%m-%d", "%Y/%m/%d"]:
        try:
            return datetime.strptime(date_str, fmt)
        except Exception:
            continue
    return pd.NaT

for df in [csv_df, excel_df, json_df]:
    df['OrderDate'] = df['OrderDate'].astype(str).apply(parse_order_date)
    df['Day'] = df['OrderDate'].dt.day
    df['Month'] = df['OrderDate'].dt.month
    df['Year'] = df['OrderDate'].dt.year
    df['OrderMonth'] = df['OrderDate'].dt.to_period('M')

 
# Step 4: CONCATENATE UNIFIED DATASETS
all_data = pd.concat([csv_df, excel_df, json_df], ignore_index=True)


# Step 5: DATA AGGREGATION TASKS
 
print('\n--- Data Aggregation Tasks ---')
# a) Total sales by product
print('\nTotal Sales by Product:')
print(all_data.groupby('Product')['Sales'].sum())

# b) Sales by category and month (pivot)
print('\nSales by Category and Month:')
pivot = all_data.pivot_table(index='Category', columns='OrderMonth', values='Sales', aggfunc='sum')
print(pivot)

# c) Count of orders per month
print('\nCount of Orders per Month:')
print(all_data.groupby('OrderMonth').size())

# d) Descriptive statistics
print('\nDescriptive Statistics:')
print(all_data.describe())

# Step 6: VISUALIZATION


#  Bar Plot: Total Sales by Category
plt.figure(figsize=(8,5))
all_data.groupby('Category')['Sales'].sum().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Sales by Product Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Pie Chart: Sales Distribution by Product
plt.figure(figsize=(7,7))
all_data.groupby('Product')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='Pastel1')
plt.title('Sales Distribution by Product')
plt.ylabel('')
plt.show()

#  Box Plot: Sales Value Distribution
plt.figure(figsize=(6,4))
plt.boxplot(all_data['Sales'], vert=False)
plt.title('Sales Value Distribution')
plt.xlabel('Sales')
plt.show()

#  Line Plot: Monthly Sales Trend
if 'OrderMonth' in all_data.columns:
    month_sales = all_data.groupby('OrderMonth')['Sales'].sum()
    month_sales.plot(kind='line', marker='o', color='teal')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid()
    plt.tight_layout()
    plt.show()

# --- Bar Plot: Number of Orders per Product
plt.figure(figsize=(8,5))
all_data['Product'].value_counts().plot(kind='bar', color='salmon')
plt.title('Number of Orders for Each Product')
plt.xlabel('Product')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()




print('\nUnified, Clean, and Aggregated Data Sample:')
print(all_data.head(12))
