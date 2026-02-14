import numpy as np
import pandas as pd

"""Task To Do:
1. Revenue = quantity × price
2. Month column
3. Year column
4. Profit margin"""

#loading dataset
print("Loading cleaned dataset...")

df = pd.read_csv('data/clean/clean_sales.csv', encoding='latin1')

print("Dataset loaded successfully!")
print(df.head())


#add column "revenue"
df["revenue"] = df["quantity"]*df["actual_price"]


#Converting Order Date
print("\nConverting date column...")
df["Order Date"] = pd.to_datetime(df["order_date"], errors="coerce")


#add month column
df["Month"] = df["Order Date"].dt.month


#add year column
df["Year"] = df["Order Date"].dt.year



output_path = "data/clean/enriched_sales.csv"

df.to_csv(output_path, index=False)

print("\nFeature engineering complete!")
print(f"Enriched dataset saved to: {output_path}")
