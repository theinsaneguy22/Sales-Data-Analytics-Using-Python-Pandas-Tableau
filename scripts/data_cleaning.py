import numpy as np
import pandas as pd

"""Task To Do:
1. Remove duplicates
2. Handle missing values
3. Fix column formats
4. Clean text columns

Save cleaned data
data/clean/clean_sales.csv"""


#loading dataset
print("Loading cleaned dataset...")

df = pd.read_csv('data/raw/amazon_sales_raw.csv', encoding='latin1')

print("Dataset loaded successfully!")
print(df.head())


#Remove duplicates
#df = df.drop_duplicates()


#Handle missing values
df.replace(
    ["NaN", "nan", "NAN", " ", "", "NULL", "null", "None", "none", "N/A", "--", "-"],
    np.nan,
    inplace=True
)

df["quantity"] = df["quantity"].fillna(0)
df["actual_price"] = df["actual_price"].fillna(0)
df = df.dropna(subset=["quantity", "actual_price"])

df = df.dropna()

print(df.isnull())
print(f'Missing values in each column Count: {df.isnull().sum()}')

# Clean actual_price (remove ₹, commas, spaces)
df["actual_price"] = (
    df["actual_price"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)



df["actual_price"] = pd.to_numeric(df["actual_price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

#Date Formatting
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Optional derived features
df["Year"] = df["order_date"].dt.year
df["Month"] = df["order_date"].dt.month
df["Day"] = df["order_date"].dt.day


#Output
output_path = "data/clean/clean_sales.csv"
df.to_csv(output_path, index=False)

print("\nData Cleaning complete!")
print(f"Cleaned dataset saved to: {output_path}")