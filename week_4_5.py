import pandas as pd

# Import listing and sold csvs from last week
sold = pd.read_csv('idx_files/w3_sold_with_rates.csv', low_memory=False)
listings = pd.read_csv('idx_files/w3_listing_with_rates.csv', low_memory=False)

# SOLD DATASET

# View Initial Sold Row Count
print('Initial Sold Row Count:', len(sold))

# Convert to Datetime
sold_cols = ['CloseDate', 'PurchaseContractDate', 'ListingContractDate', 'ContractStatusChangeDate']
sold[sold_cols] = sold[sold_cols].apply(pd.to_datetime, errors='coerce')
invalid_numeric_sold = ((sold['ClosePrice'] <= 0) |(sold['LivingArea'] <= 0) |(sold['DaysOnMarket'] < 0) 
                        |(sold['BedroomsTotal'] < 0) |(sold['BathroomsTotalInteger'] < 0))
print('Invalid Numeric Sold Columns:', invalid_numeric_sold.sum())
sold = sold.drop(sold[invalid_numeric_sold].index).reset_index(drop=True)

# Drop Redundant and Unhelpful Columns
cols_to_drop_sold = [col for col in sold.columns if sold[col].nunique() <= 1]
print('Unhelpful Sold Columns Dropped:', cols_to_drop_sold)
sold = sold.drop(columns=cols_to_drop_sold)

dot_one_cols_sold = [c for c in sold.columns if c.endswith('.1')]
explicit_redundant_sold = ['ListingId', 'ListingKeyNumeric', 'ListAgentFirstName', 'ListAgentLastName']
redundant_cols_sold = list(set(dot_one_cols_sold + [c for c in explicit_redundant_sold if c in sold.columns]))

sold = sold.drop(columns=redundant_cols_sold)
print('Redundant Sold Columns Dropped:', len(redundant_cols_sold))
print('Remaining Sold Column Count:', len(sold.columns))

# Date Consistency Checks
sold['listing_after_close_flag'] = sold['ListingContractDate'] > sold['CloseDate']
sold['purchase_after_close_flag'] = sold['PurchaseContractDate'] > sold['CloseDate']
sold['negative_timeline_flag'] = sold['PurchaseContractDate'] < sold['ListingContractDate']

# Geographic Data Checks
sold_geo_missing = sold['Latitude'].isna() | sold['Longitude'].isna()
sold_senti_null = (sold['Latitude'] == 0) | (sold['Longitude'] == 0)
sold_positive_long = sold['Longitude'] > 0

out_of_cal_flag = ((sold['Longitude'] < -124.0) | (sold['Longitude'] > -114.0) 
                   | (sold['Latitude'] < 32.0) | (sold['Latitude'] > 42.0)) & ~sold_geo_missing & ~sold_senti_null & ~sold_positive_long

# Print Sums of Geographic Data Checks
print('Missing Coordinates:', sold_geo_missing.sum())
print('Sentinel Null Values:', sold_senti_null.sum())
print('Positive Longitudinal Values:', sold_positive_long.sum())
print('Out of California Coordinates Sum:', out_of_cal_flag.sum())

# Print New Row Total
print('Row Total After Cleaning:', len(sold))

print('-'*40)

# LISTINGS DATASET

# View Initial Listings Row Count
print('Initial Listings Row Count:', len(listings))

# Convert to Datetime
listings_cols = ['ListingContractDate', 'ContractStatusChangeDate']
listings[listings_cols] = listings[listings_cols].apply(pd.to_datetime, errors='coerce')

# Filter Invalid Numeric Values
invalid_numeric_listings = ((listings['ListPrice'] <= 0) | (listings['LivingArea'] <= 0)
                        |(listings['DaysOnMarket'] < 0) | (listings['BedroomsTotal'] < 0) 
                        |(listings['BathroomsTotalInteger'] < 0))
print('Invalid Numeric Listings Columns:', invalid_numeric_listings.sum())
listings = listings.drop(listings[invalid_numeric_listings].index).reset_index(drop=True)

# Drop Redundant and Unhelpful Columns
cols_to_drop_listings = [col for col in listings.columns if listings[col].nunique() <= 1]
print('Empty/Constant Columns Dropped (Listings):', cols_to_drop_listings)
listings = listings.drop(columns=cols_to_drop_listings)

dot_one_cols_listings = [c for c in listings.columns if c.endswith('.1')]
explicit_redundant_listings = ['ListingId', 'ListingKeyNumeric', 'ListAgentFirstName', 'ListAgentLastName']
redundant_cols_listings = list(set(dot_one_cols_listings + [c for c in explicit_redundant_listings if c in listings.columns]))

listings = listings.drop(columns=redundant_cols_listings)
print('Redundant Columns Dropped (Listings):', len(redundant_cols_listings))
print('Remaining Column Count (Listings):', len(listings.columns))

# Date Consistency Checks
listings['status_before_listing_flag'] = listings['ContractStatusChangeDate'] < listings['ListingContractDate']

# Geographic Data Checks
listings_geo_missing = listings['Latitude'].isna() | listings['Longitude'].isna()
listings_senti_null = (listings['Latitude'] == 0) | (listings['Longitude'] == 0)
listings_positive_long = listings['Longitude'] > 0

out_of_cal_flag_listings = ((listings['Longitude'] < -124.0) | (listings['Longitude'] > -114.0) | 
                            (listings['Latitude'] < 32.0) | (listings['Latitude'] > 42.0))& ~listings_geo_missing & ~listings_senti_null & ~listings_positive_long

# Print Sums of Geographic Data Checks
print('Missing Coordinates:', listings_geo_missing.sum())
print('Sentinel Null Values:', listings_senti_null.sum())
print('Positive Longitudinal Values:', listings_positive_long.sum())
print('Out of California Coordinates Sum:', out_of_cal_flag_listings.sum())

# Print New Row Total
print('Row Total After Cleaning:', len(listings))

# SAVE NEW DATASETS
sold.to_csv('idx_files/w4_5_sold_cleaned.csv', index=False)
listings.to_csv('idx_files/w4_5_listing_cleaned.csv', index=False)