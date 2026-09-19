**Data Pipeline - Books to SQLite ETL**
**Overview**
This project builds an end-to-end data pipeline that scrapes book data from BooksToScrape, cleans and transforms the data, converts prices from GBP to INR, stores it in a normalized SQLite database, and performs SQL and pandas-based analysis.

**Dataset**
Source: http://books.toscrape.com/

**Fields collected:**

Title
Price (GBP)
Star Rating
Availability
Category
Data Cleaning
Converted price to price_gbp (float)
Converted ratings (One-Five) to integers (1-5)
Converted availability to boolean in_stock
Applied median imputation for numeric parsing issues
Currency Conversion
Fixed project rate:

**1 GBP = 105.50 INR**

price_inr = price_gbp * 105.50
