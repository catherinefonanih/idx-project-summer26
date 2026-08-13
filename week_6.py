import pandas as pd
import numpy as np

sold = pd.read_csv('idx_files/w4_5_sold_cleaned.csv', low_memory=False)
listings = pd.read_csv('idx_files/w4_5_listing_cleaned.csv', low_memory=False)

# Convert columns to datetime format
datecolumns = ['CloseDate', 'PurchaseContractDate', 'ListingContractDate', 'ContractStatusChangeDate']
for columns in datecolumns:
    if columns in sold.columns:
        sold[columns] = pd.to_datetime(sold[columns], errors='coerce')
    if columns in listings.columns:
        listings[columns] = pd.to_datetime(listings[columns], errors='coerce')

# Price Ratio
sold['PriceRatio'] = sold['ClosePrice']/sold['ListPrice']

# Price Per Square Feet
sold['PricePerSqFt'] = sold['ClosePrice']/sold['LivingArea']
listings['PricePerSqFt'] = listings['ListPrice']/listings['LivingArea']

# Year / Month / YrMo
sold['CloseYear'] = sold['CloseDate'].dt.year
sold['CloseMonth'] = sold['CloseDate'].dt.month
sold['CloseYrMo'] = sold['CloseDate'].dt.to_period('M').astype(str)

# Listing to Contract Days
sold['ListingToContractDays'] = (sold['PurchaseContractDate'] - sold['ListingContractDate']).dt.days

# Close to Original List Ratio
sold['CloseToOriginalListRatio'] = sold['ClosePrice'] / sold['OriginalListPrice']

# Contract to Close Days
sold['ContractToCloseDays'] = (sold['CloseDate'] - sold['PurchaseContractDate']).dt.days

# View Sample Output
print(sold[['ClosePrice', 'PriceRatio', 'PricePerSqFt', 'CloseToOriginalListRatio',
            'ListingToContractDays', 'ContractToCloseDays', 'CloseYrMo']].head())
# Segment Analysis - PropertySubType
print(sold.groupby('PropertySubType').agg(TotalSales=('ClosePrice', 'count'),
    AvgPricePerSqFt=('PricePerSqFt', 'mean'),AvgDaysOnMarket=('DaysOnMarket',
                    'mean')).reset_index().head(10))

# Segment Analysis - CountyOrParish and MLSAreaMajor
print(sold.groupby(['CountyOrParish', 'MLSAreaMajor']).agg(TotalSales=('ClosePrice', 'count'),
    AvgPricePerSqFt=('PricePerSqFt', 'mean'), AvgDaysOnMarket=('DaysOnMarket', 'mean')).reset_index().head(10))

# OfficeName and BuyerOfficeName
print(sold.groupby(['ListOfficeName', 'BuyerOfficeName']).agg(TotalSales=('ClosePrice', 'count'),
    AvgPricePerSqFt=('PricePerSqFt', 'mean'), AvgDaysOnMarket=('DaysOnMarket', 'mean')).reset_index().head(10))

# Save CSVs
sold.to_csv('idx_files/w6_sold_engineered.csv', index=False)
listings.to_csv('idx_files/w6_listing_engineered.csv', index=False)
