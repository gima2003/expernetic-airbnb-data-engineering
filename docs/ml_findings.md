# Revenue Prediction Model Results

## Linear Regression

Results:

* MAE: 10,055.51
* RMSE: 93,813.98
* R²: 0.0211

Observation:
Linear Regression showed poor predictive performance, indicating that revenue relationships are not purely linear.

---

## Random Forest Regressor

Results:

* MAE: 5,974.09
* RMSE: 86,481.47
* R²: 0.1682

Observation:
Random Forest significantly outperformed Linear Regression by capturing non-linear relationships between listing characteristics and revenue.

---

## Model Comparison

| Metric | Linear Regression | Random Forest |
| ------ | ----------------: | ------------: |
| MAE    |         10,055.51 |      5,974.09 |
| RMSE   |         93,813.98 |     86,481.47 |
| R²     |            0.0211 |        0.1682 |

Selected Model:

* Random Forest Regressor

Reason:
Random Forest achieved lower prediction errors and explained more variance in annual revenue than Linear Regression.


## Feature Importance Analysis

The Random Forest model was analyzed to identify the strongest drivers of Airbnb revenue.

Top Features:

| Feature | Importance |
|----------|----------:|
| Price | 46.71% |
| Average Review Length | 21.24% |
| Number of Reviews | 9.24% |
| Review Score Rating | 5.26% |
| Review Text Count | 5.24% |
| Occupancy Rate | 4.15% |

Key Insight:

Price was the strongest predictor of annual revenue. Review-related features collectively contributed over 40% of predictive power, suggesting that guest engagement and customer satisfaction significantly influence listing performance.

Business Recommendation:

Hosts should focus not only on pricing strategy but also on improving guest experience and review quality to maximize annual revenue.

## Model Persistence

The final selected Random Forest Regressor was serialized using Pickle and stored in:

models/revenue_predictor.pkl

Purpose:
- Reuse trained model without retraining
- Integrate into Streamlit dashboard
- Support future prediction requests

Selected Model:
- Random Forest Regressor

Reason:
- Lowest MAE
- Lowest RMSE
- Highest R² score among evaluated models

## Price Recommendation Dataset

A separate dataset was prepared for price recommendation modeling.

Steps:
- Selected listing characteristics and host attributes.
- Used price as the target variable.
- Removed records with missing target values.
- Applied 99th percentile capping to remove extreme outlier prices.

Dataset Statistics:
- Records: 61,350
- Features: 12
- Target: Price (£)
- Price Cap Applied: £1,100

Reason:
Extreme luxury listings distorted the price distribution and negatively impacted model training.
## Price Recommendation Train-Test Split

Dataset Split:
- Training records: 49,080
- Testing records: 12,270

Configuration:
- Test Size: 20%
- Random State: 42

Purpose:
The split ensures unbiased evaluation of price prediction performance on unseen listings.

## Price Recommendation Model

Dataset Preparation:
- Target Variable: Price (£)
- Records: 61,350
- Features: 12
- Price Outliers Removed Using 99th Percentile
- Price Cap Applied: £1,100

Train-Test Split:
- Training Records: 49,080
- Testing Records: 12,270

Model:
- Random Forest Regressor
- Number of Trees: 100
- Random State: 42

Status:
- Model Training Completed Successfully
- Evaluation Pending

### Price Recommendation Model Results

Model:
- Random Forest Regressor
- 100 Trees

Performance:

MAE: 55.70

RMSE: 99.45

R² Score: 0.5781

Interpretation:

The model explains approximately 57.8% of the variation in Airbnb listing prices.

On average, predicted prices differ from actual listing prices by approximately £56 per night.

The pricing model significantly outperformed the revenue prediction model and demonstrated strong predictive capability using listing, host, review, and location features.

### Feature Importance Analysis

The most influential factors affecting Airbnb pricing were:

1. Bedrooms (24.7%)
2. Host Experience (12.4%)
3. Bathrooms (11.9%)
4. Occupancy Rate (10.6%)

Location-based variables such as Westminster and Kensington & Chelsea also contributed significantly to pricing decisions.

The results suggest that property size, host maturity, occupancy performance, and premium locations are the primary drivers of Airbnb prices in London.

## Price Recommendation Model

Dataset:
- Records: 61,350
- Features: 12
- Target: Price (£)

Model:
- Random Forest Regressor
- 100 Trees

Results:
- MAE: 55.70
- RMSE: 99.45
- R²: 0.5781

Top Features:
1. Bedrooms (24.7%)
2. Host Experience Years (12.4%)
3. Bathrooms (11.9%)
4. Occupancy Rate (10.6%)
5. Average Review Length (5.3%)

Model File:
- price_recommender.pkl

## Saved Model Files

Both trained machine learning models were successfully serialized using Joblib.

Saved Models:
- models/revenue_predictor.pkl
- models/price_recommender.pkl

File Verification:
- revenue_predictor.pkl: successfully saved after correcting initial empty file issue
- price_recommender.pkl: successfully saved

Purpose:
These saved models can be reused in the Streamlit dashboard without retraining.

## Revenue Prediction Model Comparison

| Model | MAE | RMSE | R² |
|---------|---------|---------|---------|
| Linear Regression | 10055.51 | 93813.98 | 0.021 |
| Random Forest | 5974.09 | 86481.47 | 0.168 |
| Gradient Boosting | 6745.94 | 65011.86 | 0.530 |

Best Model:

Gradient Boosting Regressor

Key Findings:

- Linear Regression performed poorly due to weak linear relationships in the dataset.
- Random Forest improved predictive performance by capturing non-linear interactions.
- Gradient Boosting achieved the highest explanatory power with an R² score of 0.530.
- Revenue prediction is influenced by complex interactions among listing characteristics, reviews, occupancy, and pricing variables.

## Residual Analysis

Gradient Boosting Residual Summary

- Mean Residual: 224.84
- Median Residual: -334.28
- Standard Deviation: 65,014
- Minimum Residual: -5,057,387
- Maximum Residual: 4,851,349

Interpretation:

The residual mean was close to zero, indicating that the model does not exhibit substantial systematic bias.

However, several very large residuals were observed, reflecting the presence of extreme revenue outliers within the Airbnb dataset.

These outliers contributed to elevated prediction error variance and cross-validation instability.


## Model Comparison

Three regression model families were evaluated for annual Airbnb revenue prediction.

| Model | R² | RMSE | MAE |
|---------|---------:|---------:|---------:|
| Linear Regression | 0.021 | 93,814 | 10,056 |
| Random Forest | 0.168 | 86,481 | 5,974 |
| Gradient Boosting | 0.530 | 65,012 | 6,746 |

Findings:

- Linear Regression showed very poor predictive performance, indicating that the relationship between the selected features and annual revenue is highly non-linear.
- Random Forest improved prediction accuracy substantially compared to Linear Regression.
- Gradient Boosting achieved the highest R² score and lowest RMSE, making it the best-performing model.
- Therefore, Gradient Boosting was selected as the final model for deployment in the Streamlit dashboard.

## SHAP Explainability

SHAP analysis was applied to the Gradient Boosting revenue prediction model to improve model transparency.

Top Features Identified:

1. Number of Reviews
2. Price
3. Review Text Count
4. Host Experience Years
5. Superhost Status
6. Accommodates
7. Occupancy Rate
8. Room Type
9. Neighbourhood

Business Interpretation:

The model places high importance on demand-related variables such as number of reviews and review text count. This suggests that listings with stronger booking and review activity tend to have more predictable revenue patterns.

Price was also a key driver, confirming that nightly pricing strategy directly influences annual revenue. Host experience and Superhost status contributed to the model, indicating that host credibility and operational maturity affect performance.

SHAP improved model interpretability by showing which features most influenced revenue predictions.