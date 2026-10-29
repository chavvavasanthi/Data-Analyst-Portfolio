# Retail Customer Data Cleaning Using Python

## Project Overview
This project focuses on cleaning retail customer data using Python and Pandas. The goal is to improve data quality and prepare the dataset for further analysis.

## Tools Used
- Python
- Pandas
- Microsoft Excel
- CSV files

## Data Cleaning Steps
- Removed completely empty rows.
- Removed extra empty columns.
- Removed rows with missing CustomerID.
- Removed exact duplicate records.
- Cleaned customer names and city names.
- Standardized email addresses to lowercase.
- Converted Age and PurchaseAmount into numeric values.
- Handled missing text values.
- Filled missing ages using the average age.
- Preserved missing purchase amounts instead of inventing values.

## Project Results
- Original dataset: 21 rows.
- Cleaned dataset: 19 rows.
- Final columns: 7.
- Missing PurchaseAmount values: 2.

## Files Included
- `customer_data_raw.csv` — Original dataset.
- `customer_data_cleaned.csv` — Cleaned dataset.
- `data_cleaning.py` — Python cleaning script.

## Conclusion
This project demonstrates basic data cleaning, missing-value handling, text standardization, and data quality checks using Python and Pandas.
