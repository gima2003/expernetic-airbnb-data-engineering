## Dataset Profiling - Listings Table

Date: Today

Dataset: London Airbnb Listings

### Dataset Size
- Rows: 96,871
- Columns: 79

### Duplicate Analysis
- Duplicate Records: 0
- Observation: No fully duplicated listing records found.

### Missing Values
- price: 34,908 missing (36.04%)
- beds: 34,920 missing
- bathrooms: 34,846 missing
- host_about: 47,038 missing

### Initial Business Interpretation
A significant proportion of listings are missing pricing and property details. Data cleaning and validation will be required before analytics or machine learning can be performed.

### Calendar Dataset Observation

calendar.csv contains 35.3 million records.

This table represents daily availability records and is significantly larger than the other datasets.

Transformations and aggregations should be performed before joining with listings data to avoid excessive memory usage.

Data Cleaning Decision

license column has 100% missing values.

Decision:
Drop column from analytical dataset because it contains no usable information.

### Cleaning Decision - Listings Table

Removed three columns with 100% missing values:
- license
- calendar_updated
- neighbourhood_group_cleansed

Reason:
These columns contained no usable information for analysis, modeling, or reporting.

Cleaned the price column by removing currency symbols and commas, then converting it to numeric format.

### Cleaning Decision - Listings Table

Removed three columns with 100% missing values:
- license
- calendar_updated
- neighbourhood_group_cleansed

Reason:
These columns contained no usable information for analysis, modeling, or reporting.

Cleaned the price column by removing currency symbols and commas, then converting it to numeric format.

## Dataset Relationship Analysis

### Primary Keys

* listings.id

### Foreign Keys

* calendar.listing_id → listings.id
* reviews.listing_id → listings.id

### Relationship Structure

Listings has a one-to-many relationship with Calendar.

One listing can have many daily availability records.

Listings has a one-to-many relationship with Reviews.

One listing can have many customer reviews.

Neighbourhood information can be linked through neighbourhood-related columns in listings.

---

## Dataset Size Summary

| Dataset        |       Rows | Columns |
| -------------- | ---------: | ------: |
| Listings       |     96,871 |      79 |
| Calendar       | 35,357,974 |       7 |
| Reviews        |  2,097,996 |       6 |
| Neighbourhoods |         33 |       2 |

### Observation

Calendar is significantly larger than all other datasets and contains over 35 million records.

Aggregations should be performed before joining this table to avoid excessive memory usage and slow processing.

---

## Price Column Investigation

### Finding

Price values are stored as text.

Examples:

* $70.00
* $149.00
* $411.00

### Data Engineering Decision

Remove currency symbols and convert values into numeric format.

Reason:

Statistical analysis, SQL aggregations, and machine learning models require numeric values.

---

## Cleaning Decisions

### Removed Columns

* license
* calendar_updated
* neighbourhood_group_cleansed

### Reason

These columns contain 100% missing values and provide no analytical value.

### Result

Listings dataset reduced from:

* 79 columns

to:

* 76 columns

without losing useful information.

---

## Dataset Limitations

1. Price column contains 36.04% missing values.
2. Beds column contains 36.05% missing values.
3. Bathrooms column contains 35.97% missing values.
4. Several review score columns contain approximately 25% missing values.
5. Calendar dataset size may create performance challenges during processing.
6. Some host-related descriptive fields contain large amounts of missing information.

---

## Initial Assumptions

1. Missing prices are treated as unavailable pricing information unless recovered from calendar data.
2. Listings without reviews may represent new properties rather than poor-quality listings.
3. Calendar availability records accurately reflect booking availability.
4. Listing IDs uniquely identify Airbnb properties.
5. Review records are assumed to belong to valid listings.


## Validation Results - Listings Table

Validation checks were performed on the cleaned listings dataset.

### Results
- Negative prices: 0
- Negative bedrooms: 0
- Negative bathrooms: 0
- Duplicate listing IDs: 0

### Interpretation
The cleaned listings dataset passed the initial core validation checks. No invalid negative numerical values or duplicate listing identifiers were detected.


## Transformation Result - Calendar Summary

The raw calendar dataset contained 35,357,974 daily records.

To make it usable for analytics, the calendar data was aggregated to listing level.

Generated metrics:
- available_days
- booked_days
- total_calendar_days
- avg_calendar_price
- occupancy_rate
- estimated_revenue

The transformed calendar summary contains 96,871 rows, matching the listing-level granularity.

## Master Dataset Creation

Listings and Calendar Summary datasets were merged using:

listings.id = calendar_summary.listing_id

Join Type:
- Left Join

Result:
- Rows: 96,871
- Columns: 83

The master dataset combines:
- Property information
- Host information
- Review metrics
- Availability metrics
- Occupancy metrics
- Revenue estimates

Output:
data/processed/airbnb_master.csv