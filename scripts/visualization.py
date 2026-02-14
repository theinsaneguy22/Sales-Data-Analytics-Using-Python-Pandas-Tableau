import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/enriched_sales.csv")

#Monthly revenue trend
df["Month"] = pd.to_datetime(df["Month"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
monthly = df.groupby(df["Month"])["revenue"].sum()
monthly.plot(title="Monthly Sales")
plt.title("Monthly Revenue Trend")
plt.savefig("visualizations/monthly_trend.png")
plt.close()


#Revenue by rating
rating_rev = df.groupby("rating")["revenue"].sum()
rating_rev.plot(kind="bar")
plt.title("Revenue by Rating")
plt.savefig("visualizations/revenue_rating.png")
plt.close()



#Discount vs revenue
plt.scatter(
    df["discount_percentage"],
    df["revenue"]
)
plt.title("Discount vs Revenue")
plt.savefig("visualizations/discount_vs_sales.png")
plt.close()



#Product performance
top = df.groupby("product_name")["revenue"].sum().sort_values(ascending=False).head(5)

top.plot(kind="bar")
plt.title("Top Products")
plt.savefig("visualizations/top_products.png")
plt.close()




#Rating distribution
df["rating"].hist()
plt.title("Rating Distribution")
plt.savefig("visualizations/rating_distribution.png")
plt.close()



print("\nData Visualization complete!")