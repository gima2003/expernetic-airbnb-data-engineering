# Engineering Decision Log

## Decision 1: City Selection

### Options Considered

* Multiple cities
* Single city (London)

### Decision

Selected London as the primary market.

### Rationale

London contains a large and diverse Airbnb marketplace with sufficient listing, review, and calendar data to support comprehensive engineering, analytics, and machine learning workflows.

### Trade-Off

A single-city analysis limits cross-market comparisons but allows deeper analysis within the available timeframe.

---

## Decision 2: Calendar Data Aggregation

### Options Considered

* Join raw calendar data directly
* Aggregate calendar data before joining

### Decision

Aggregated calendar records to listing level before integration.

### Rationale

The calendar dataset contained over 35 million records. Direct joins would significantly increase processing time and memory consumption.

### Trade-Off

Daily-level detail was sacrificed in favor of improved analytical performance.

---

## Decision 3: Database Selection

### Options Considered

* PostgreSQL
* DuckDB
* SQLite

### Decision

SQLite

### Rationale

SQLite provided a lightweight analytical environment suitable for assignment requirements while supporting dimensional modeling and SQL analytics.

### Trade-Off

SQLite is less scalable than enterprise database platforms.

---

## Decision 4: Machine Learning Models

### Options Considered

* Linear Regression
* Random Forest
* Gradient Boosting

### Decision

Evaluated all three models and selected Gradient Boosting for revenue prediction.

### Rationale

Gradient Boosting achieved the highest R² score and lowest RMSE.

### Trade-Off

Model interpretability is lower than Linear Regression.

---

## Decision 5: Explainable AI

### Options Considered

* Feature Importance Only
* SHAP Explainability

### Decision

Implemented SHAP analysis.

### Rationale

SHAP provides transparent explanations of feature contributions and improves stakeholder trust.

### Trade-Off

Additional computational overhead was introduced.

---

## Decision 6: Dashboard Framework

### Options Considered

* Power BI
* Dash
* Streamlit

### Decision

Streamlit

### Rationale

Streamlit enables rapid development of interactive dashboards using Python and integrates easily with machine learning workflows.

### Trade-Off

Less enterprise-ready than Power BI or commercial BI platforms.
