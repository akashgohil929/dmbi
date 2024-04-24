import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv('expt4.csv')
# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(df['Product Category'], df['Sales (in thousands)'])
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Sales (in thousands)')
plt.xticks(rotation=45)
plt.show()
# Box Plot
plt.figure(figsize=(8, 6))
plt.boxplot(df['Profit Margin (%)'], labels=['Profit Margin'])
plt.title('Profit Margin Distribution by Product Category')
plt.ylabel('Profit Margin (%)')
plt.show()
# Histogram
plt.figure(figsize=(8, 6))
plt.hist(df['Sales (in thousands)'], bins=10, edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales (in thousands)')
plt.ylabel('Frequency')
plt.show()
# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Sales (in thousands)'], df['Profit Margin (%)'])
plt.title('Sales vs. Profit Margin')
plt.xlabel('Sales (in thousands)')
plt.ylabel('Profit Margin (%)')
plt.show()