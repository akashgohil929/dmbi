import pandas as pd
import numpy as np
# Read the data from the "Expt3.csv" file
df = pd.read_csv('Expt3.csv')
# Display the original data
print("Original Data:")
print(df)
# Handling Missing Data
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Price'].fillna(df['Price'].mean(), inplace=True)
# Handling missing data for nominal columns by replacing with mode
df['Color'].fillna(df['Color'].mode()[0], inplace=True)
df['Size'].fillna(df['Size'].mode()[0], inplace=True)
# Data Transformation - Binning and Replacing Noisy Data
average_price = df[df['Price'] != 4500]['Price'].mean()
df['Price'] = df['Price'].replace(4500, average_price)
# Display the preprocessed data
print("\nPreprocessed Data:")
print(df)