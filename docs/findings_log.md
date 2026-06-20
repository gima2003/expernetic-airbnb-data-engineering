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

## EDA Finding - Room Type Distribution

Entire home/apartment listings dominate the London Airbnb market with 62,907 listings.

Private rooms account for 33,643 listings.

Shared rooms and hotel rooms represent less than 1% of total supply.

Business Interpretation:

London Airbnb is primarily a full-property rental marketplace rather than a room-sharing platform.

## EDA Finding - Listing Concentration

Westminster contains the largest number of Airbnb listings (11,385), making it the largest Airbnb market in London.

Tower Hamlets, Camden, Kensington and Chelsea, and Hackney also show significant Airbnb activity.

Business Interpretation:

Airbnb supply is concentrated in central and highly visited London boroughs where tourism and business travel demand are strongest.

## EDA Finding - Pricing

Tower Hamlets shows the highest average Airbnb price (£430.91).

However, the pricing distribution is highly skewed by premium listings and luxury properties.

Median price analysis is recommended alongside average price analysis.

## EDA Finding - Price Outliers

Several listings contain extremely high prices.

Examples:
- £1,085,147
- £74,100
- £66,189

These values are significantly higher than typical Airbnb nightly prices and create a highly right-skewed distribution.

Impact:
- Distorts average price calculations
- Affects visualizations
- Can negatively influence machine learning models

Recommendation:
Use outlier treatment before modeling and dashboard development.

## EDA Finding - Price Distribution

Median Price: £135
Average Price: £229.92

The average price is significantly higher than the median price.

Interpretation:
The London Airbnb market exhibits a right-skewed price distribution due to high-priced luxury listings and extreme outliers.

Percentile Analysis:
- 25% of listings cost less than £77
- 50% cost less than £135
- 75% cost less than £221
- 95% cost less than £500
- 99% cost less than £1100

Recommendation:
Use median values and percentile-based filtering when building machine learning models.

## EDA Finding - Listing Density by Borough

Top Boroughs by Number of Airbnb Listings:

1. Westminster - 11,385 listings
2. Tower Hamlets - 7,469 listings
3. Camden - 6,551 listings
4. Kensington and Chelsea - 6,401 listings
5. Hackney - 6,359 listings

Interpretation:

Central London boroughs dominate the Airbnb market.

Westminster alone contains over 11,000 active listings and represents the highest concentration of Airbnb activity.

Implication:

Location is likely one of the strongest drivers of occupancy and revenue.

## EDA Finding - Premium Boroughs

Top Boroughs by Average Airbnb Price:

1. Tower Hamlets (£430.91)
2. City of London (£354.39)
3. Lambeth (£345.71)
4. Westminster (£342.14)
5. Kensington and Chelsea (£336.07)

Interpretation:

Premium Airbnb pricing is concentrated in central London boroughs.

Tower Hamlets shows the highest average listing price, potentially influenced by luxury apartments and premium short-term rental properties.

Business Implication:

Location is a significant factor affecting Airbnb pricing and potential host revenue.

## EDA Finding - Occupancy Analysis

Average Occupancy Rate: 60.28%

Median Occupancy Rate: 73.70%

Observation:

A significant number of listings show 100% occupancy.

Possible explanations:

- Highly demanded properties
- Host-blocked calendars
- Long-term reservations
- Availability management strategies

Business Implication:

Occupancy rate is a critical KPI because it directly influences host revenue and platform utilization.

## EDA Finding - Price vs Occupancy

Correlation between Price and Occupancy Rate:

-0.0103

Interpretation:

There is almost no linear relationship between listing price and occupancy rate.

The scatter plot shows that both high-priced and low-priced listings can achieve high occupancy.

Business Implication:

Pricing alone does not determine booking success. Other factors such as location, room type, reviews, host reputation, and amenities likely have a stronger impact on occupancy.

### Revenue Dataset Observation

Two revenue-related columns were identified:

- estimated_revenue_l365d
- estimated_revenue

Findings:

- estimated_revenue contains 100% missing values and provides no analytical value.
- estimated_revenue_l365d contains 61,963 populated records and can be used for revenue analysis.

Decision:
The column estimated_revenue will be excluded from subsequent analysis and modelling activities.

### Revenue Analysis

Average annual revenue was analysed using the estimated_revenue_l365d field.

Top Revenue Generating Boroughs:

1. Lambeth (£21,777)
2. Westminster (£16,809)
3. Kensington and Chelsea (£15,367)
4. City of London (£13,741)
5. Camden (£13,074)

Business Insight:

- Lambeth generates the highest annual Airbnb revenue.
- Westminster contains the highest number of listings but ranks second in revenue.
- Tower Hamlets has the highest average listing price but does not produce the highest revenue.
- Revenue appears to be influenced by both pricing strategy and occupancy levels rather than price alone.

### Dataset Integration Update

The final master dataset was enhanced by integrating:

- listings_cleaned.csv
- calendar_summary.csv
- reviews_summary.csv
- neighbourhoods.csv

Join Keys:
- listings.id = calendar_summary.listing_id
- listings.id = reviews_summary.listing_id
- listings.neighbourhood_cleansed = neighbourhoods.neighbourhood

Final Master Dataset:
- Rows: 96,871
- Columns: 89

This consolidated dataset will be used for feature engineering, dashboard development, and machine learning modeling.

## Feature Engineering Results

### Revenue Categories

- Low Revenue Listings: 22,906
- No Revenue Listings: 21,046
- Medium Revenue Listings: 10,960
- High Revenue Listings: 7,051

Observation:
A large proportion of listings generate little or no annual revenue, while a relatively small segment contributes high revenue.

### Price Categories

- Standard: 27,144
- Budget: 22,429
- Premium: 9,334
- Luxury: 3,055

Observation:
Standard and Budget properties dominate the London Airbnb market.

### Host Experience

Average Host Experience:
- Mean: 8.4 years
- Median: 9.3 years

Observation:
Most Airbnb hosts have several years of hosting experience, indicating a mature marketplace.

### Review Lifetime

Average Review Lifetime:
- Mean: 731 days
- Median: 357 days

Observation:
Many listings remain active and receive reviews over multiple years.

## Data Modeling & Warehousing Findings

### Star Schema Design

A star schema was implemented using SQLite to support analytical querying and future dashboard development.

#### Fact Table

* fact_listing_metrics

  * listing_id
  * host_id
  * neighbourhood_cleansed
  * price
  * availability_365
  * occupancy_rate
  * estimated_revenue_l365d
  * number_of_reviews
  * review_scores_rating

#### Dimension Tables

* dim_listing
* dim_host
* dim_neighbourhood

### Database Summary

| Table                | Records |
| -------------------- | ------: |
| fact_listing_metrics |  96,871 |
| dim_listing          |  96,871 |
| dim_host             |  55,646 |
| dim_neighbourhood    |      33 |

### SQL Analysis Results

#### Highest Revenue Boroughs

1. Lambeth (£21,777 avg annual revenue)
2. Westminster (£16,809 avg annual revenue)
3. Kensington and Chelsea (£15,367 avg annual revenue)

Observation:
Central London boroughs generate significantly higher annual revenue than outer boroughs.

#### Room Type Analysis

| Room Type       | Avg Price (£) | Avg Occupancy (%) |
| --------------- | ------------: | ----------------: |
| Hotel Room      |        657.83 |             47.53 |
| Entire Home/Apt |        279.35 |             59.17 |
| Private Room    |        121.71 |             62.55 |
| Shared Room     |         96.91 |             37.66 |

Observation:
Private rooms achieve the highest occupancy rates, while hotel rooms command premium pricing but lower occupancy.

### Data Warehouse Notes

The calendar dataset was aggregated into listing-level metrics before warehouse loading. Therefore, a date dimension table was not required for the current analytical model.

For a production-scale Airbnb warehouse, a dim_date table and daily booking fact table would be recommended.


## Machine Learning Dataset Preparation

### Revenue Prediction Dataset

Created a machine learning dataset from the feature-engineered Airbnb dataset.

Target Variable:

* estimated_revenue_l365d

Selected Features:

* price
* bedrooms
* bathrooms
* accommodates
* review_scores_rating
* occupancy_rate
* number_of_reviews
* review_text_count
* avg_review_length
* host_experience_years
* room_type
* neighbourhood_cleansed
* host_is_superhost

Dataset Shape:

* Original featured dataset: 96,871 rows × 93 columns
* Revenue prediction dataset: 61,963 rows × 14 columns

Missing Values Observed:

* bedrooms: 114
* bathrooms: 76
* review_scores_rating: 13,908
* review_text_count: 13,908
* avg_review_length: 13,908
* host_experience_years: 25
* host_is_superhost: 1,352

Observation:
A significant number of listings have no review history, causing missing values in review-related features. Missing values will be handled using imputation during model training rather than removing records.


### Train-Test Split

The revenue prediction dataset was divided into training and testing datasets.

Dataset Statistics:

* Total records: 61,963
* Training records: 49,570 (80%)
* Testing records: 12,393 (20%)
* Features used: 13

Approach:

* Used train_test_split() from Scikit-Learn
* Test size = 20%
* Random State = 42 for reproducibility

Reason:
The split ensures that model performance is evaluated on unseen data and prevents overfitting.


### Linear Regression Evaluation

Model:

* Linear Regression

Evaluation Results:

* MAE: 10,055.51
* RMSE: 93,813.98
* R²: 0.0211

Interpretation:

The model demonstrated weak predictive performance. An R² score of 0.021 indicates that only a small portion of revenue variability is explained by the selected features.

Possible Reasons:

* Revenue relationships are non-linear.
* Location and occupancy effects interact in complex ways.
* Outliers and high-revenue listings influence predictions.

Decision:
A more advanced tree-based model will be evaluated.
