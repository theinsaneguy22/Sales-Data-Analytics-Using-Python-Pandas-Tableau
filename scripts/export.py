import pandas as pd

df = pd.read_csv("data/clean/enriched_sales.csv")

df.to_csv(
    "data/clean/tableau_ready.csv",
    index=False
)

print("Dataset ready for Tableau!")
