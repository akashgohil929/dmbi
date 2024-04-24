# Step 1: Importing the required libraries
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
# Step 2: Loading and exploring the data
data = pd.read_csv("expt8.csv")
# data = pd.read_excel('Online_Retail.xlsx')
data.head()
# Step 3: Cleaning the Data
data['Description'] = data['Description'].str.strip()
data.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
data['InvoiceNo'] = data['InvoiceNo'].astype('str')
data = data[~data['InvoiceNo'].str.contains('C')]
# Step 4: Splitting the data according to the region of transaction
basket_France = (data[data['Country'] =="France"]

.groupby(['InvoiceNo', 'Description'])['Quantity']
.sum().unstack().reset_index().fillna(0)
.set_index('InvoiceNo'))

# Step 5: Hot encoding the Data
def hot_encode(x):
    if(x<= 0):
        return 0
    if(x>= 1):
        return 1
basket_encoded = basket_France.applymap(hot_encode)
basket_France = basket_encoded
# Step 6: Building the models and analyzing the results
frq_items = apriori(basket_France, min_support=0.05, use_colnames=True)
rules = association_rules(frq_items, metric="lift", min_threshold=1)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
print(rules.head())