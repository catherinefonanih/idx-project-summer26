import pandas as pd

# import our saved csv files from last week
listing = pd.read_csv('idx_files/w2_residential_listing.csv')
sold = pd.read_csv('idx_files/w2_residential_sold.csv')

# fetch the mortgage csv from FRED
df_mortgage = pd.read_csv('idx_files/MORTGAGE30US.csv', parse_dates=['observation_date'])
df_mortgage.columns = ['date', 'rate_30yr_fixed']

# resampling weekly rates to monthly averages
df_mortgage['year_month'] = df_mortgage['date'].dt.to_period('M')
monthly = df_mortgage.groupby('year_month')['rate_30yr_fixed'].agg('mean').reset_index()

# key off CloseDate
sold['year_month'] = pd.to_datetime(sold['CloseDate']).dt.to_period('M')

# key off ListingContractDate
listing['year_month'] = pd.to_datetime(listing['ListingContractDate']).dt.to_period('M')

# merge listing and sold with mortgages
sold_rates = sold.merge(monthly, on='year_month', how='left')
listing_rates = listing.merge(monthly, on='year_month', how='left')

# validate merge (check for null values)
print(sold_rates.rate_30yr_fixed.isna().sum())
print(listing_rates.rate_30yr_fixed.isna().sum())

# preview
print(sold_rates[['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']].head(16))
print(listing_rates[['ListingContractDate', 'year_month', 'ListPrice', 'rate_30yr_fixed']].head(16))

# save
sold_rates.to_csv('idx_files/w3_sold_with_rates.csv', index=False)
listing_rates.to_csv('idx_files/w3_listing_with_rates.csv', index=False)