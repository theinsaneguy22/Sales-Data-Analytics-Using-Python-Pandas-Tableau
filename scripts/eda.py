import numpy as np
import pandas as pd

"""Task To Do:
        Import pandas (DONE)
        Read CSV (DONE)
        Print first rows (DONE)
        Print dataset shape (DONE)
        Check column names
        Check missing values """

#Read CSV
df = pd.read_csv('data/raw/amazon_sales_raw.csv', encoding='latin1')

#Data information
print(df.info())

#Print first rows
print(df.head())

#Print dataset shape
print(f'shape: {df.shape}')

#Check column names
print(f'column names: {df.columns}')

#Check missing values
print(df.isnull())

print(f'Missing values in each column Count: {df.isnull().sum()}')



print("\nData Exploration complete!")