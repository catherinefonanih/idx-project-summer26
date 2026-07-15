import pandas as pd

# Create DataFrames with Each Listing File from January 2024 to Most Recent
listing01 = pd.read_csv('idx_files/CRMLSListing202401.csv')
listing02 = pd.read_csv('idx_files/CRMLSListing202402.csv')
listing03 = pd.read_csv('idx_files/CRMLSListing202403.csv')
listing04 = pd.read_csv('idx_files/CRMLSListing202404.csv')
listing05 = pd.read_csv('idx_files/CRMLSListing202405.csv')
listing06 = pd.read_csv('idx_files/CRMLSListing202406.csv')
listing07 = pd.read_csv('idx_files/CRMLSListing202407.csv')
listing08 = pd.read_csv('idx_files/CRMLSListing202408.csv')
listing09 = pd.read_csv('idx_files/CRMLSListing202409.csv')
listing10 = pd.read_csv('idx_files/CRMLSListing202410.csv')
listing11 = pd.read_csv('idx_files/CRMLSListing202411.csv')
listing12 = pd.read_csv('idx_files/CRMLSListing202412.csv')
listing13 = pd.read_csv('idx_files/CRMLSListing202501.csv')
listing14 = pd.read_csv('idx_files/CRMLSListing202502.csv')
listing15 = pd.read_csv('idx_files/CRMLSListing202503.csv')
listing16 = pd.read_csv('idx_files/CRMLSListing202504.csv')
listing17 = pd.read_csv('idx_files/CRMLSListing202505.csv')
listing18 = pd.read_csv('idx_files/CRMLSListing202506.csv')
listing19 = pd.read_csv('idx_files/CRMLSListing202507.csv')
listing20 = pd.read_csv('idx_files/CRMLSListing202508.csv')
listing21 = pd.read_csv('idx_files/CRMLSListing202509.csv')
listing22 = pd.read_csv('idx_files/CRMLSListing202510.csv')
listing23 = pd.read_csv('idx_files/CRMLSListing202511.csv')
listing24 = pd.read_csv('idx_files/CRMLSListing202512.csv')
listing25 = pd.read_csv('idx_files/CRMLSListing202601.csv')
listing26 = pd.read_csv('idx_files/CRMLSListing202602.csv')
listing27 = pd.read_csv('idx_files/CRMLSListing202603.csv')
listing28 = pd.read_csv('idx_files/CRMLSListing202604.csv')
listing29 = pd.read_csv('idx_files/CRMLSListing202605.csv', encoding='cp1252')
listing30 = pd.read_csv('idx_files/CRMLSListing202606.csv', encoding='cp1252')


# count and print rows before concatenation
listing_rows = (len(listing01) + len(listing02)+ len(listing03) + len(listing04) + len(listing05) + len(listing06) + len(listing07)
                +  len(listing08) + len(listing09) + len(listing10) + len(listing11) + len(listing12) + len(listing13) + len(listing14)
                +  len(listing15) + len(listing16) + len(listing17) + len(listing18) + len(listing19) + len(listing20) + len(listing21)
                +  len(listing22) + len(listing23) + len(listing24) + len(listing25) + len(listing26) + len(listing27) + len(listing28)
                +  len(listing29) + len(listing30))
print('Initial Listing Row Total:', listing_rows)

# count and print rows after concatenation
listing = pd.concat([listing01, listing02, listing03, listing04, listing05, listing06, listing07, 
                           listing08, listing09, listing10, listing11, listing12, listing13, listing14,
                           listing15, listing16, listing17, listing18, listing19, listing20, listing21,
                           listing22, listing23, listing24, listing25, listing26, listing27, listing28,
                           listing29, listing30])
print('Listing Row Total After Concatenation:', len(listing))

# count and print rows after filtering for residential
residential_listing = listing[listing.PropertyType == 'Residential']
print('Listing Row Total After Residential Filter:', len(residential_listing))


# Create DataFrames with Each Sold File from January 2024 to Most Recent
sold01 = pd.read_csv('idx_files/CRMLSSold202401.csv')
sold02 = pd.read_csv('idx_files/CRMLSSold202402.csv')
sold03 = pd.read_csv('idx_files/CRMLSSold202403.csv')
sold04 = pd.read_csv('idx_files/CRMLSSold202404.csv')
sold05 = pd.read_csv('idx_files/CRMLSSold202405_filled.csv').drop(columns = ['latfilled', 'lonfilled'])
sold06 = pd.read_csv('idx_files/CRMLSSold202406_filled.csv').drop(columns = ['latfilled', 'lonfilled'])
sold07 = pd.read_csv('idx_files/CRMLSSold202407_filled.csv').drop(columns = ['latfilled', 'lonfilled'])
sold08 = pd.read_csv('idx_files/CRMLSSold202408.csv')
sold09 = pd.read_csv('idx_files/CRMLSSold202409.csv')
sold10 = pd.read_csv('idx_files/CRMLSSold202410.csv')
sold11 = pd.read_csv('idx_files/CRMLSSold202411.csv')
sold12 = pd.read_csv('idx_files/CRMLSSold202412.csv')
sold13 = pd.read_csv('idx_files/CRMLSSold202501_filled.csv').drop(columns = ['latfilled', 'lonfilled'])
sold14 = pd.read_csv('idx_files/CRMLSSold202502.csv')
sold15 = pd.read_csv('idx_files/CRMLSSold202503.csv')
sold16 = pd.read_csv('idx_files/CRMLSSold202504.csv')
sold17 = pd.read_csv('idx_files/CRMLSSold202505.csv')
sold18 = pd.read_csv('idx_files/CRMLSSold202506.csv')
sold19 = pd.read_csv('idx_files/CRMLSSold202507.csv')
sold20 = pd.read_csv('idx_files/CRMLSSold202508.csv')
sold21 = pd.read_csv('idx_files/CRMLSSold202509.csv')
sold22 = pd.read_csv('idx_files/CRMLSSold202510.csv')
sold23 = pd.read_csv('idx_files/CRMLSSold202511.csv')
sold24 = pd.read_csv('idx_files/CRMLSSold202512.csv')
sold25 = pd.read_csv('idx_files/CRMLSSold202601.csv')
sold26 = pd.read_csv('idx_files/CRMLSSold202602.csv')
sold27 = pd.read_csv('idx_files/CRMLSSold202603.csv')
sold28 = pd.read_csv('idx_files/CRMLSSold202604.csv')
sold29 = pd.read_csv('idx_files/CRMLSSold202605.csv', encoding = 'cp1252')
sold30 = pd.read_csv('idx_files/CRMLSSold202606.csv', encoding='cp1252')

# count and print rows before concatenation
sold_rows = (len(sold01) + len(sold02) + len(sold03) + len(sold04) + len(sold05) + len(sold06) + len(sold07)
        +   len(sold08) + len(sold09) + len(sold10) + len(sold11) + len(sold12) + len(sold13) + len(sold14)
        +   len(sold15) + len(sold16) + len(sold17) + len(sold18) + len(sold19) + len(sold20) + len(sold21)
        +   len(sold22) + len(sold23) + len(sold24) + len(sold25) + len(sold26) + len(sold27) + len(sold28)
        +   len(sold29) + len(sold30))
print('Initial Sold Row Total:', sold_rows)

# count and print rows after concatenation
sold = pd.concat([sold01, sold02, sold03, sold04, sold05, sold06, sold07,
                sold08, sold09, sold10,sold11, sold12, sold13, sold14,
                sold15, sold16, sold17, sold18, sold19, sold20, sold21,
                sold22, sold23, sold24, sold25, sold26, sold27, sold28,
                sold29, sold30])
print('Sold Row Total After Concatenation:', len(sold))

# count and print rows after filtering for residential
residential_sold = sold[sold.PropertyType == 'Residential']
print('Sold Row Total After Residential Filter:', len(residential_sold))

# save as csv files
residential_listing.to_csv('idx_files/w1_residential_listings.csv', index=False)
residential_sold.to_csv('idx_files/w1_residential_sold.csv', index=False)