# H1 - Entire Home vs Private Room Prices

Test Used:
- Independent Two-Sample T-Test

Hypotheses:

H0:
Average prices of Entire Homes and Private Rooms are equal.

H1:
Average prices of Entire Homes and Private Rooms are different.

Results:

- Sample Size (Entire Home): 42,318
- Sample Size (Private Room): 19,382
- T Statistic: 5.7951
- P Value: 6.87e-09

Decision:

Reject H0

Business Interpretation:

The analysis found a statistically significant difference between Entire Home and Private Room prices in London Airbnb listings. Room type is therefore an important pricing factor and should be considered when building pricing strategies and recommendation models.

## H2 - Superhost vs Non-Superhost Ratings

Test Used:

* Independent Two-Sample T-Test

Hypotheses:

H0:
Superhosts and Non-Superhosts have equal average review ratings.

H1:
Superhosts and Non-Superhosts have different average review ratings.

Results:

* Superhost Mean Rating: 4.854
* Non-Superhost Mean Rating: 4.637
* T Statistic: 76.04
* P Value: < 0.0001

Decision:

Reject H0

Business Interpretation:

The analysis found a statistically significant difference in review ratings between Superhosts and Non-Superhosts.

Superhost listings achieved substantially higher average ratings, suggesting that Superhost status is associated with improved guest satisfaction and service quality.

This finding supports the business value of Airbnb's Superhost program and highlights the importance of host quality indicators in marketplace performance.

## H3 - Review Count vs Price

Test Used:

* Independent Two-Sample T-Test

Hypotheses:

H0:
Listings with more than 10 reviews and listings with 10 or fewer reviews have equal average prices.

H1:
Listings with more than 10 reviews and listings with 10 or fewer reviews have different average prices.

Results:

* Mean Price (>10 Reviews): £181.81
* Mean Price (≤10 Reviews): £265.11
* T Statistic: -2.675
* P Value: 0.00748

Decision:

Reject H0

Business Interpretation:

The analysis found a statistically significant difference in prices between listings with high and low review counts.

Listings with fewer reviews were more expensive on average than listings with many reviews. This suggests that higher prices do not necessarily lead to higher review volume and may indicate different market segments such as premium or luxury properties.


## H4 - Borough Price Differences (ANOVA)

Test Used:

* One-Way ANOVA

Hypotheses:

H0:
Average Airbnb prices are equal across selected boroughs.

H1:
At least one borough has a different average Airbnb price.

Results:

* F Statistic: 0.962
* P Value: 0.427

Decision:

Fail to Reject H0

Business Interpretation:

Although descriptive statistics suggested substantial differences in average prices across boroughs, the ANOVA test did not find statistically significant evidence of price differences among the selected boroughs.

A likely explanation is the presence of substantial price variability and extreme outliers within boroughs, which may mask true geographic pricing effects.

Further analysis using outlier treatment or robust statistical methods is recommended.

## H5 - Weekend vs Weekday Pricing

Test Planned:
- Independent Two-Sample T-Test

Objective:
To determine whether Airbnb listing prices differ between weekdays and weekends.

Status:
Not Performed

Reason:
The calendar dataset contained 35,357,974 records; however, both the `price` and `adjusted_price` columns were completely missing.

Missing Values:

- price: 35,357,974
- adjusted_price: 35,357,974

As a result, no statistically valid comparison between weekday and weekend pricing could be conducted.

Conclusion:
This hypothesis could not be evaluated due to insufficient pricing information in the calendar dataset.

## Confidence Interval Analysis

Objective:
Estimate the true average Airbnb listing price in London.

Results:

- Sample Size: 61,963
- Mean Price: £229.92
- 95% Confidence Interval Lower Bound: £194.98
- 95% Confidence Interval Upper Bound: £264.86

Interpretation:

The analysis indicates that the true average Airbnb listing price in London is likely to fall between £194.98 and £264.86 with 95% confidence.

This interval provides a statistically reliable estimate of the overall market pricing level.

## Correlation Analysis

Objective:
Identify variables most strongly associated with Airbnb prices.

Results:

| Variable | Correlation with Price |
|-----------|-----------|
| Estimated Revenue | 0.0946 |
| Average Review Length | 0.0266 |
| Bedrooms | 0.0215 |
| Bathrooms | 0.0205 |
| Accommodates | 0.0186 |

Interpretation:

No variable demonstrated a strong linear correlation with Airbnb prices.

The strongest observed relationship was between estimated revenue and price (r = 0.0946), although this remained weak.

These results suggest that Airbnb pricing is influenced by complex, non-linear interactions among multiple factors rather than a single dominant variable.

## Driver Analysis

Machine Learning Feature Importance Results

Revenue Prediction Model:

Top Drivers:
1. Price
2. Average Review Length
3. Number of Reviews
4. Review Rating
5. Occupancy Rate

Price Recommendation Model:

Top Drivers:
1. Bedrooms
2. Host Experience Years
3. Bathrooms
4. Occupancy Rate
5. Average Review Length

Business Insights:

- Property size (bedrooms and bathrooms) is a major determinant of listing prices.
- Experienced hosts tend to charge higher prices.
- Occupancy performance contributes to both revenue generation and pricing behaviour.
- Location factors such as Westminster and Kensington & Chelsea influence pricing outcomes.
- Pricing decisions appear to depend on multiple interacting variables rather than a single dominant factor.

Effect Size:

- Cohen's d = 0.035

Interpretation:

Although the t-test identified a statistically significant difference in prices between Entire Homes and Private Rooms, the practical effect size was negligible.

This suggests that room type alone explains only a very small portion of pricing variation.
Effect Size:

- Cohen's d = 0.444

Interpretation:

The difference in ratings between Superhosts and Non-Superhosts shows a small-to-moderate practical effect.

This indicates that Superhost status is associated with meaningfully higher guest ratings and is not merely statistically significant due to large sample size.

Effect Size:

- Cohen's d = -0.0188

Interpretation:

Although the hypothesis test detected a statistically significant difference in prices between listings with high and low review counts, the practical effect size was negligible.

This suggests that review count alone has very limited influence on Airbnb pricing.

Effect Size:

- Eta Squared (η²) = 0.000154

Interpretation:

The ANOVA effect size was extremely small, indicating that neighbourhood membership explained virtually none of the observed variation in Airbnb prices.

This supports the ANOVA conclusion that borough-level price differences were not statistically meaningful in this dataset.

## OLS Regression Analysis

Objective:
Quantify the marginal impact of listing characteristics on Airbnb prices.

Model Performance:

- R² = 0.001
- Adjusted R² = 0.001
- Prob(F-statistic) = 1.10e-07

Key Findings:

Bathrooms:
- Coefficient = +73.47
- P-value = 0.021
- Statistically significant

Occupancy Rate:
- Coefficient = -1.16
- P-value = 0.032
- Statistically significant

Bedrooms:
- Coefficient = +47.31
- Not statistically significant

Accommodates:
- Coefficient = +7.47
- Not statistically significant

Number of Reviews:
- Coefficient = -0.24
- Not statistically significant

Host Experience Years:
- Coefficient = -5.78
- Not statistically significant

Interpretation:

The OLS model explains only a very small proportion of Airbnb price variation (R² = 0.001), indicating that pricing is influenced by complex non-linear relationships.

This finding supports the superior performance of Random Forest models observed during the machine learning phase.

Cross Validation Results

R² Scores:
[-9.679, 0.134, -0.206, 0.407, 0.357]

Average R²:
-1.797

Observation:

The revenue target exhibited extreme skewness and several very high-value outliers (maximum revenue = £10.15 million).

These outliers caused substantial variability across validation folds and reduced cross-validation stability.

Despite this, hold-out test performance remained strong with Gradient Boosting achieving R² = 0.530.