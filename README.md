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

**Database Schema**
categories
category_id (PK)
category_name
books
book_id (PK)
title
price_gbp
price_inr
rating
in_stock
category_id (FK)

**SQL Queries Performed**
SELECT + WHERE
ORDER BY
LIMIT
DISTINCT
BETWEEN / IN

**JOIN between books and categories**
Pandas Validation
Loaded query results using pd.read_sql()
Recreated JOIN using pd.merge()
Verified both outputs matched

**Results**
Books scraped: ...
Categories scraped: ...
Database tables: 2
SQL queries executed: 5+
JOIN validation completed


**Design Decisions**
SQLite used for simplicity and portability.
Normalized schema reduces data redundancy.
Median imputation prevents pipeline failures from malformed values.
