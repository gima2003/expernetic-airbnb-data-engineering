# 🏠 London Airbnb Market Intelligence Platform

An end-to-end Data Engineering, Analytics, Statistical Analysis, and Machine Learning project built using the London Inside Airbnb dataset.

This project was developed as part of the Expernetic Data Engineer Internship Technical Assessment and demonstrates the complete data lifecycle from raw data ingestion to business intelligence dashboards and predictive machine learning models.

---

## 🎯 Project Objectives

The goal of this project is to transform raw Airbnb marketplace data into actionable business intelligence for:

- Revenue Strategists
- Product Managers
- Market Analysts
- Operations Teams
- Airbnb Hosts

The platform provides:

✅ Data Engineering Pipeline

✅ Exploratory Data Analysis

✅ Statistical Analysis

✅ Revenue Prediction Model

✅ Price Recommendation Engine

✅ Model Explainability using SHAP

✅ Interactive Streamlit Dashboard

---

# 📂 Dataset

Source:

Inside Airbnb Public Dataset

City Selected:

📍 London, United Kingdom

Files Used:

| File | Purpose |
|--------|----------|
| listings.csv | Listing information |
| reviews.csv | Guest review data |
| calendar.csv | Availability data |
| neighbourhoods.csv | Borough information |

Dataset Size:

- 96,871 Listings
- 35+ Million Calendar Records
- Thousands of Reviews

---

# 🏗️ Project Architecture

Raw Data
↓
Data Cleaning
↓
Feature Engineering
↓
Master Dataset
↓
SQLite Data Warehouse
↓
EDA & Statistics
↓
Machine Learning Models
↓
SHAP Explainability
↓
Streamlit Dashboard

---

# ⚙️ Data Engineering

## Data Ingestion

Implemented ingestion workflows for:

- Listings Dataset
- Reviews Dataset
- Calendar Dataset
- Neighbourhood Dataset

## Data Cleaning

Performed:

- Missing value handling
- Duplicate detection
- Data validation
- Data type standardization
- Price conversion
- Date standardization

## Feature Engineering

Created:

- Occupancy Rate
- Estimated Annual Revenue
- Host Experience Years
- Review Text Count
- Average Review Length
- Price Per Bedroom

Output:

```text
data/processed/airbnb_featured.csv
```

---

# 🗄️ Data Modeling

Implemented analytical data model using SQLite.

### Fact Tables

- Fact Listings

### Dimension Tables

- Dim Host
- Dim Neighbourhood
- Dim Room Type

Benefits:

- Faster analytical querying
- Structured reporting
- Improved scalability

---

# 📊 Exploratory Data Analysis

Key analyses performed:

### Room Type Analysis

- Entire homes dominate the London market

### Borough Analysis

- Westminster contains the highest listing density

### Pricing Analysis

- Highly right-skewed distribution
- Presence of premium luxury listings

### Occupancy Analysis

- Significant variation across neighbourhoods

---

# 📈 Statistical Analysis

## Hypothesis Testing

### H1 – Entire Home vs Private Room Prices

Result:

✅ Statistically Significant Difference

### H2 – Superhost vs Non-Superhost Ratings

Result:

✅ Superhosts receive significantly higher ratings

### H3 – Review Count vs Price

Result:

✅ Significant relationship detected

### H4 – Borough Price Differences

Result:

❌ No significant borough-level differences detected

### H5 – Weekend vs Weekday Pricing

Result:

⚠ Could not be evaluated due to missing calendar pricing fields

---

## Additional Statistical Work

- Confidence Intervals
- Effect Size Analysis
- Correlation Analysis
- OLS Regression
- Cross Validation Analysis

---

# 🤖 Machine Learning

## Problem 1

### Revenue Prediction

Target:

```text
estimated_revenue_l365d
```

Models Compared:

- Linear Regression
- Random Forest
- Gradient Boosting

Results:

| Model | R² |
|---------|---------|
| Linear Regression | 0.021 |
| Random Forest | 0.168 |
| Gradient Boosting | 0.530 |

🏆 Best Model:

Gradient Boosting Regressor

---

## Problem 2

### Price Recommendation

Target:

```text
price
```

Model:

Random Forest Regressor

Purpose:

Recommend optimal nightly Airbnb prices based on listing characteristics.

---

# 🔍 Model Explainability

Implemented SHAP (SHapley Additive Explanations).

### Top Revenue Drivers

1. Number of Reviews
2. Price
3. Review Text Count
4. Host Experience
5. Occupancy Rate

Generated:

```text
reports/shap_summary.png
```

Benefits:

- Transparent predictions
- Explainable AI
- Feature importance visualization

---

# 📊 Interactive Dashboard

Built using Streamlit.

Features:

### Executive Overview

- Total Listings
- Average Price
- Average Revenue
- Occupancy Rate

### Market Analytics

- Room Type Analysis
- Borough Analysis
- Price Distribution
- Occupancy Distribution

### Revenue Predictor

Predict annual Airbnb revenue.

### Price Recommender

Recommend nightly Airbnb pricing.

### SHAP Explainability

Visual explanation of model predictions.

---

# 🛠️ Technology Stack

## Languages

- Python
- SQL

## Libraries

- Pandas
- NumPy
- Scikit-Learn
- StatsModels
- SciPy
- SHAP
- Plotly
- Streamlit
- Joblib

## Database

- SQLite

## Version Control

- Git
- GitHub

---

# 📁 Project Structure

```text
expernetic-airbnb-data-engineering
│
├── dashboard/
│ └── app.py
│
├── data/
│ ├── raw/
│ └── processed/
│
├── database/
│
├── docs/
│ ├── findings_log.md
│ ├── ml_findings.md
│ ├── statistical_findings.md
│ └── project_plan.md
│
├── models/
│ ├── revenue_predictor.pkl
│ └── price_recommender.pkl
│
├── notebooks/
│ ├── 01_dataset_understanding.ipynb
│ ├── 02_eda.ipynb
│ ├── 03_feature_engineering.ipynb
│ ├── 04_data_modeling.ipynb
│ └── 05_machine_learning.ipynb
│
├── reports/
│ └── shap_summary.png
│
└── README.md
```

---

# 🚀 Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run dashboard:

```bash
streamlit run dashboard/app.py
```

---

# 📌 Key Business Insights

- Superhost status strongly influences guest ratings.
- Entire-home listings command premium pricing.
- Pricing behaviour is influenced by multiple interacting factors.
- Occupancy and review activity are major revenue drivers.
- Machine learning significantly outperforms traditional linear models.


---

# 👩‍💻 Author

Gimhani Pabodha

BSc (Hons) Information Technology – Data Science

SLIIT University

---

# ⭐ Project Highlights

✔ End-to-End Data Engineering

✔ Statistical Hypothesis Testing

✔ Machine Learning Pipeline

✔ SHAP Explainable AI

✔ Streamlit Dashboard

✔ Real-World Airbnb Dataset

✔ Business Intelligence Focus
