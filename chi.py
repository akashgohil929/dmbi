import pandas as pd
from scipy.stats import chi2_contingency
df = pd.read_csv('expt4.csv')

# Create a contingency table
contingency_table = pd.crosstab(df['Sales (in thousands)'], df['Profit Margin(%)'])
# Perform the Chi-Square test
chi2_statistic, p_value, dof, _ = chi2_contingency(contingency_table)
# Print the results
print(f"Chi2 Statistic: {chi2_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")
# Interpret the results based on the p-value
alpha = 0.05
if p_value > alpha:
    print("Accept the null hypothesis (variables are independent)")
else:
    print("Reject the null hypothesis (variables are dependent)")
# Calculate the correlation coefficient
correlation_matrix = df[['Sales (in thousands)', 'Profit Margin (%)']].corr()
correlation_coefficient = correlation_matrix.iloc[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient:.4f}")