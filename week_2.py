import pandas as pd

sold = pd.read_csv('idx_files/w1_residential_sold.csv')
listing = pd.read_csv('idx_files/w1_residential_listings.csv')

sold['PropertyType'].unique()
listing['PropertyType'].unique()

# because this dataset is already filtered to residential property types, we will focus on all residential types this week

# Sold CSV

# observations
print(sold.shape)

print(sold.dtypes)

sold.head()

# missing count and percentages
missing_sum_sold = sold.isna().sum()
print(missing_sum_sold)
missing_sold_percentage = (sold.isna().mean())*100
print(missing_sold_percentage)

# high missing columns
col_sold = missing_sold_percentage[missing_sold_percentage>90].index
print(col_sold)

# drop columns with missing values over 90%
sold = sold.drop(columns = col_sold)

# summary for all numeric fields
num_fields_sold= ['ClosePrice', 'LivingArea', 'DaysOnMarket']
print(sold[num_fields_sold].describe())


# Listing CSV

# observations
print(listing.shape)

print(listing.dtypes)

listing.head()

# missing count and percentages
missing_sum_listing = listing.isna().sum()
print(missing_sum_listing)
missing_listing_percentage = (listing.isna().mean())*100
print(missing_listing_percentage)

# high missing columns
col_listing = missing_listing_percentage[missing_listing_percentage>90].index
print(col_listing)

# drop columns with missing values over 90%
listing = listing.drop(columns = col_listing)

# summary for all numeric fields
num_fields_list = ['ListPrice', 'LivingArea', 'DaysOnMarket']
print(listing[num_fields_list].describe())

sold.to_csv('idx_files/w2_residential_sold.csv', index=False)
listing.to_csv('idx_files/w2_residential_listing.csv', index=False)