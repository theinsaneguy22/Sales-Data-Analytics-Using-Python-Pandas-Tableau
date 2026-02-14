import numpy as np
import pandas as pd

#loading dataset
print("Loading cleaned dataset...")
df = pd.read_csv('data/clean/enriched_sales.csv', encoding='latin1')
print("Dataset loaded successfully!")
print(df.head())


#Calculate Total Revenue
total_revenue = df["revenue"].sum()
pd.DataFrame({"Total Revenue": [total_revenue]}).to_csv("reports/total_revenue.csv", index=False)


#monthly sales
monthly_sales = df.groupby("Month")["revenue"].sum()
monthly_sales.to_csv("reports/monthly_sales.csv")

#top discounted product
top_discounted_prod = df.groupby("product_name")["discount_percentage"].head(10)
top_discounted_prod.to_csv("reports/top_discounted_prod.csv")

#average rating
df["rating"] = df["rating"].replace(["NAN", "nan", "NaN", ""], np.nan)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
avg_rating = df["rating"].mean()
pd.DataFrame({"Average Rating": [avg_rating]}).to_csv(
    "reports/average_rating.csv", index=False
)

#revenue by rating
rev_by_rating = df.groupby("rating")["revenue"].sum()
rev_by_rating.to_csv("reports/revenue_by_rating.csv")

# top selling products
top_selling_prod = df.groupby("product_name")["revenue"].sum().sort_values(ascending=False).head(10)
top_selling_prod.to_csv("reports/top_selling_prod.csv")


print("\nData Analysis complete!")

