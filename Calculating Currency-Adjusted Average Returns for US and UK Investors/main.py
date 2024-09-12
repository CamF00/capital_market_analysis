import pandas as pd

# Given data
data = {
    'Period': [1, 2, 3, 4, 5, 6],
    'US Return': [None, 0.06, 0.12, -0.05, 0.15, 0.10],
    'UK Return': [None, 0.05, 0.10, -0.03, 0.12, 0.10],
    'Exchange Rate (USD/GBP)': [1.30, 1.35, 1.32, 1.30, 1.35, 1.30]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Calculate returns for a US investor investing in the UK market
df['Return for US Investor in UK'] = (1 + df['UK Return']) * (df['Exchange Rate (USD/GBP)'] / df['Exchange Rate (USD/GBP)'].shift(1)) - 1

# Calculate returns for a UK investor investing in the US market
df['Return for UK Investor in US'] = (1 + df['US Return']) * (df['Exchange Rate (USD/GBP)'].shift(1) / df['Exchange Rate (USD/GBP)']) - 1

# Calculate the average returns
average_return_us_investor_uk = df['Return for US Investor in UK'].mean()
average_return_uk_investor_us = df['Return for UK Investor in US'].mean()

average_return_us_investor_uk, average_return_uk_investor_us
