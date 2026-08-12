import pandas as pd

sold = pd.read_csv('idx_files/w6_sold_engineered.csv')
listings = pd.read_csv('idx_files/w6_listing_engineered.csv')

# Counts Before Filter
print('Sold Row and Column Count:', sold.shape)
print('Listing Row and Column Count:', listings.shape)
print('Sold ClosePrice Median:', sold['ClosePrice'].median())
print('Sold LivingArea Median:', sold['LivingArea'].median())
print('Sold DaysOnMarket Median:', sold['DaysOnMarket'].median())
print('Listing LivingArea Median:', listings['LivingArea'].median())
print('Listing DaysOnMarket Median:', listings['DaysOnMarket'].median())

print('-' * 80)

# FIND OUTLIER VALUES

# Sold Dataset Outliers
# ClosePrice outliers
print(sold['ClosePrice'].describe())

cprice_q1 = sold['ClosePrice'].quantile(0.25)
cprice_q3 = sold['ClosePrice'].quantile(0.75)
cprice_iqr = cprice_q3 - cprice_q1
print('ClosePrice Interquartile Range:', cprice_iqr)

cprice_upper = cprice_q3 + (1.5 * cprice_iqr)
print('ClosePrice Upper Limit:', cprice_upper)

cprice_lower = cprice_q1 - (1.5 * cprice_iqr)
print('ClosePrice Lower Limit:', cprice_lower)

# LivingArea outliers
sold_area_q1 = sold['LivingArea'].quantile(0.25)
sold_area_q3 = sold['LivingArea'].quantile(0.75)
print(sold['LivingArea'].describe())

sold_area_iqr = sold_area_q3 - sold_area_q1
print('Sold LivingArea Interquartile Range:', sold_area_iqr)

sold_area_upper = sold_area_q3 + (1.5 * sold_area_iqr)
print('Sold LivingArea Upper Limit:', sold_area_upper)

sold_area_lower = sold_area_q1 - (1.5 * sold_area_iqr)
print('Sold LivingArea Lower Limit:', sold_area_lower)

# DaysOnMarket outliers
sold_days_q1 = sold['DaysOnMarket'].quantile(0.25)
sold_days_q3 = sold['DaysOnMarket'].quantile(0.75)
print(sold['DaysOnMarket'].describe())

sold_days_iqr = sold_days_q3 - sold_days_q1
print('Sold DaysOnMarket Interquartile Range:', sold_days_iqr)

sold_days_upper = sold_days_q3 + (1.5 * sold_days_iqr)
print('Sold DaysOnMarket Upper Limit:', sold_days_upper)

sold_days_lower = sold_days_q1 - (1.5 * sold_days_iqr)
print('Sold DaysOnMarket Lower Limit:', sold_days_lower)

print('-' * 80)

# Listing Dataset Outliers
# LivingArea Outliers
listings_area_q1 = listings['LivingArea'].quantile(0.25)
listings_area_q3 = listings['LivingArea'].quantile(0.75)
print(listings['LivingArea'].describe())

listings_area_iqr = listings_area_q3 - listings_area_q1
print('Listings LivingArea Interquartile Range:', listings_area_iqr)

listings_area_upper = listings_area_q3 + (1.5 * listings_area_iqr)
print('Listings LivingArea Upper Limit:', listings_area_upper)

listings_area_lower = listings_area_q1 - (1.5 * listings_area_iqr)
print('Listings LivingArea Lower Limit:', listings_area_lower)

# DaysOnMarket outliers
listings_days_q1 = listings['DaysOnMarket'].quantile(0.25)
listings_days_q3 = listings['DaysOnMarket'].quantile(0.75)
print(listings['DaysOnMarket'].describe())

listings_days_iqr = listings_days_q3 - listings_days_q1
print('Listings DaysOnMarket Interquartile Range:', listings_days_iqr)

listings_days_upper = listings_days_q3 + (1.5 * listings_days_iqr)
print('Listings DaysOnMarket Upper Limit:', listings_days_upper)

listings_days_lower = listings_days_q1 - (1.5 * listings_days_iqr)
print('Listings DaysOnMarket Lower Limit:', listings_days_lower)

print('-' * 80)

# FLAGGED OUTLIERS

# Sold flagged outliers
sold['ClosePrice_outlier'] = (sold['ClosePrice'] > cprice_upper) | (sold['ClosePrice'] < cprice_lower)
sold['LivingArea_outlier'] = (sold['LivingArea'] > sold_area_upper) | (sold['LivingArea'] < sold_area_lower)
sold['DaysOnMarket_outlier'] = (sold['DaysOnMarket'] > sold_days_upper) | (sold['DaysOnMarket'] < sold_days_lower)
sold['is_outlier'] = sold['ClosePrice_outlier'] | sold['LivingArea_outlier'] | sold['DaysOnMarket_outlier']

# Listings flagged outliers
listings['LivingArea_outlier'] = (listings['LivingArea'] > listings_area_upper) | (listings['LivingArea'] < listings_area_lower)
listings['DaysOnMarket_outlier'] = (listings['DaysOnMarket'] > listings_days_upper) | (listings['DaysOnMarket'] < listings_days_lower)
listings['is_outlier'] = listings['LivingArea_outlier'] | listings['DaysOnMarket_outlier']

print('-' * 80)

# NEW FILTERED DATASETS

sold_filtered = sold[~sold['is_outlier']].copy()
sold_filtered = sold_filtered.drop(columns = ['is_outlier', 'ClosePrice_outlier', 'LivingArea_outlier', 'DaysOnMarket_outlier'])
listings_filtered = listings[~listings['is_outlier']].copy()
listings_filtered = listings_filtered.drop(columns = ['is_outlier', 'LivingArea_outlier', 'DaysOnMarket_outlier'])

# Counts After Filter
print('Sold Row and Column Count:', sold_filtered.shape)
print('Listing Row and Column Count:', listings_filtered.shape)
print('Sold ClosePrice Median:', sold_filtered['ClosePrice'].median())
print('Sold LivingArea Median:', sold_filtered['LivingArea'].median())
print('Sold DaysOnMarket Median:', sold_filtered['DaysOnMarket'].median())
print('Listing LivingArea Median:', listings_filtered['LivingArea'].median())
print('Listing DaysOnMarket Median:', listings_filtered['DaysOnMarket'].median())

# SAVE DATASETS
# Flagged
sold.to_csv('idx_files/w7_sold_flagged.csv', index=False)
listings.to_csv('idx_files/w7_listings_flagged.csv', index=False)

# Filtered
sold_filtered.to_csv('idx_files/w7_sold_filtered.csv', index=False)
listings_filtered.to_csv('idx_files/w7_listings_filtered.csv', index=False)