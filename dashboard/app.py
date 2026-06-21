import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from pathlib import Path

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="London Airbnb Intelligence Dashboard",
    page_icon="🏠",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[1]

# =========================
# Load Data & Models
# =========================
@st.cache_data
def load_data():
    return pd.read_csv(BASE_DIR / "data/processed/airbnb_featured.csv")

@st.cache_resource
def load_models():
    revenue_model = joblib.load(BASE_DIR / "models/revenue_predictor.pkl")
    price_model = joblib.load(BASE_DIR / "models/price_recommender.pkl")
    return revenue_model, price_model

data = load_data()
revenue_model, price_model = load_models()

# =========================
# Styling
# =========================
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 4px;
}
.subtitle {
    font-size: 18px;
    color: #9ca3af;
    margin-bottom: 20px;
}
.metric-card {
    background-color: #111827;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #374151;
}
.result-box {
    padding: 28px;
    border-radius: 18px;
    background-color: #064e3b;
    border: 1px solid #10b981;
    text-align: center;
    margin-top: 20px;
}
.info-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #374151;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.markdown("""
    <div style="padding: 12px 0 24px 0;">
        <h1 style="font-size: 30px; margin-bottom: 0;">🏠 Airbnb BI</h1>
        <p style="color:#9ca3af; font-size:14px; margin-top:4px;">
        London Market Intelligence Platform
        </p>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "🏡 Executive Overview",
            "📊 Market Analytics",
            "💰 Revenue Predictor",
            "🏷️ Price Recommender",
            "📐 Statistical Insights",
            "🤖 ML Model Insights",
            "🧩 Project Architecture"
        ]
    )

    st.divider()

    st.markdown("""
    <div style="font-size:13px; color:#9ca3af; line-height:1.6;">
    <b>Tech Stack</b><br>
    Python · Pandas · SQL<br>
    Statistics · Machine Learning<br>
    SHAP · Streamlit
    </div>
    """, unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown('<div class="main-title">London Airbnb Market Intelligence Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Data Engineering • Analytics • Statistics • Machine Learning</div>', unsafe_allow_html=True)
st.divider()

# =========================
# Page 1: Executive Overview
# =========================
if page == "🏡 Executive Overview":
    st.header("Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Listings", f"{data.shape[0]:,}")
    col2.metric("Average Price", f"£{data['price'].mean():.2f}")
    col3.metric("Average Occupancy", f"{data['occupancy_rate'].mean():.2f}%")
    col4.metric("Average Revenue", f"£{data['estimated_revenue_l365d'].mean():.2f}")

    st.subheader("Market Snapshot")

    c1, c2 = st.columns(2)

    with c1:
        room_counts = data["room_type"].value_counts().reset_index()
        room_counts.columns = ["Room Type", "Listings"]

        fig = px.bar(
            room_counts,
            x="Room Type",
            y="Listings",
            title="Listings by Room Type",
            text_auto=True
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        top_boroughs = data["neighbourhood_cleansed"].value_counts().head(10).reset_index()
        top_boroughs.columns = ["Borough", "Listings"]

        fig = px.bar(
            top_boroughs,
            x="Borough",
            y="Listings",
            title="Top 10 Boroughs by Listings",
            text_auto=True
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Dataset Preview")
    st.dataframe(data.head(20), use_container_width=True)

# =========================
# Page 2: Market Analytics
# =========================
elif page == "📊 Market Analytics":
    st.header("Market Analytics")

    selected_borough = st.selectbox(
        "Filter by Borough",
        ["All"] + sorted(data["neighbourhood_cleansed"].dropna().unique())
    )

    filtered_data = data.copy()

    if selected_borough != "All":
        filtered_data = filtered_data[
            filtered_data["neighbourhood_cleansed"] == selected_borough
        ]

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(
            filtered_data,
            x="price",
            nbins=50,
            title="Price Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            filtered_data,
            x="occupancy_rate",
            nbins=40,
            title="Occupancy Rate Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        avg_price = (
            filtered_data.groupby("room_type")["price"]
            .mean()
            .reset_index()
            .sort_values("price", ascending=False)
        )

        fig = px.bar(
            avg_price,
            x="room_type",
            y="price",
            title="Average Price by Room Type",
            text_auto=".2f"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        revenue_borough = (
            data.groupby("neighbourhood_cleansed")["estimated_revenue_l365d"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            revenue_borough,
            x="neighbourhood_cleansed",
            y="estimated_revenue_l365d",
            title="Top 10 Boroughs by Estimated Revenue",
            text_auto=".2f"
        )
        st.plotly_chart(fig, use_container_width=True)

# =========================
# Page 3: Revenue Predictor
# =========================
elif page == "💰 Revenue Predictor":
    st.header("Annual Revenue Predictor")
    st.write("Estimate annual Airbnb revenue using the trained Gradient Boosting revenue prediction model.")

    with st.form("revenue_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            price = st.number_input("Nightly Price (£)", min_value=0.0, value=150.0)
            bedrooms = st.number_input("Bedrooms", min_value=0.0, value=1.0)
            bathrooms = st.number_input("Bathrooms", min_value=0.0, value=1.0)
            accommodates = st.number_input("Accommodates", min_value=1, value=2)

        with col2:
            room_type = st.selectbox("Room Type", sorted(data["room_type"].dropna().unique()))
            neighbourhood = st.selectbox("Borough", sorted(data["neighbourhood_cleansed"].dropna().unique()))
            host_is_superhost = st.selectbox("Superhost", ["t", "f"])
            host_experience_years = st.number_input("Host Experience Years", min_value=0.0, value=3.0)

        with col3:
            review_scores_rating = st.number_input("Review Rating", min_value=0.0, max_value=5.0, value=4.8)
            number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=25)

            with st.expander("Advanced Inputs"):
                occupancy_rate = st.number_input("Occupancy Rate (%)", min_value=0.0, max_value=100.0, value=60.0)
                review_text_count = st.number_input("Review Text Count", min_value=0, value=25)
                avg_review_length = st.number_input("Average Review Length", min_value=0.0, value=250.0)

        submitted = st.form_submit_button("Predict Annual Revenue")

    if submitted:
        input_df = pd.DataFrame([{
            "price": price,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "accommodates": accommodates,
            "review_scores_rating": review_scores_rating,
            "occupancy_rate": occupancy_rate,
            "number_of_reviews": number_of_reviews,
            "review_text_count": review_text_count,
            "avg_review_length": avg_review_length,
            "host_experience_years": host_experience_years,
            "room_type": room_type,
            "neighbourhood_cleansed": neighbourhood,
            "host_is_superhost": host_is_superhost
        }])

        prediction = revenue_model.predict(input_df)[0]

        st.markdown(
            f"""
            <div class="result-box">
                <h2>Predicted Annual Revenue</h2>
                <h1>£{prediction:,.2f}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# Page 4: Price Recommender
# =========================
elif page == "🏷️ Price Recommender":
    st.header("Price Recommender")
    st.write("Recommend a nightly Airbnb price using the trained Random Forest pricing model.")

    with st.form("price_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            bedrooms = st.number_input("Bedrooms", min_value=0.0, value=1.0, key="p_bedrooms")
            bathrooms = st.number_input("Bathrooms", min_value=0.0, value=1.0, key="p_bathrooms")
            accommodates = st.number_input("Accommodates", min_value=1, value=2, key="p_accommodates")

        with col2:
            room_type = st.selectbox("Room Type", sorted(data["room_type"].dropna().unique()), key="p_room")
            neighbourhood = st.selectbox("Borough", sorted(data["neighbourhood_cleansed"].dropna().unique()), key="p_borough")
            host_is_superhost = st.selectbox("Superhost", ["t", "f"], key="p_superhost")

        with col3:
            review_scores_rating = st.number_input("Review Rating", min_value=0.0, max_value=5.0, value=4.8, key="p_rating")
            number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=25, key="p_reviews")

            with st.expander("Advanced Inputs"):
                occupancy_rate = st.number_input("Occupancy Rate (%)", min_value=0.0, max_value=100.0, value=60.0, key="p_occupancy")
                review_text_count = st.number_input("Review Text Count", min_value=0, value=25, key="p_review_text_count")
                avg_review_length = st.number_input("Average Review Length", min_value=0.0, value=250.0, key="p_avg_review")
                host_experience_years = st.number_input("Host Experience Years", min_value=0.0, value=3.0, key="p_host_exp")

        submitted = st.form_submit_button("Recommend Price")

    if submitted:
        input_df = pd.DataFrame([{
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "accommodates": accommodates,
            "review_scores_rating": review_scores_rating,
            "occupancy_rate": occupancy_rate,
            "number_of_reviews": number_of_reviews,
            "review_text_count": review_text_count,
            "avg_review_length": avg_review_length,
            "host_experience_years": host_experience_years,
            "room_type": room_type,
            "neighbourhood_cleansed": neighbourhood,
            "host_is_superhost": host_is_superhost
        }])

        prediction = price_model.predict(input_df)[0]

        st.markdown(
            f"""
            <div class="result-box">
                <h2>Recommended Nightly Price</h2>
                <h1>£{prediction:,.2f}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# Page 5: Statistical Insights
# =========================
elif page == "📐 Statistical Insights":
    st.header("Statistical Insights")

    st.subheader("Hypothesis Testing Summary")

    stats_table = pd.DataFrame({
        "Hypothesis": [
            "H1: Entire Home vs Private Room Prices",
            "H2: Superhost vs Non-Superhost Ratings",
            "H3: Review Count vs Price",
            "H4: Borough Price Differences",
            "H5: Weekend vs Weekday Pricing"
        ],
        "Test": [
            "Independent T-Test",
            "Independent T-Test",
            "Independent T-Test",
            "ANOVA",
            "Not Performed"
        ],
        "Result": [
            "Significant",
            "Significant",
            "Significant",
            "Not Significant",
            "Calendar prices missing"
        ],
        "Business Meaning": [
            "Room type affects pricing",
            "Superhosts achieve higher ratings",
            "Review count groups differ in price, but effect is small",
            "Borough differences were not statistically strong",
            "Could not be tested due to missing calendar prices"
        ]
    })

    st.dataframe(stats_table, use_container_width=True)

    st.subheader("Confidence Interval")

    st.info(
        "The estimated average Airbnb price in London is £229.92, "
        "with a 95% confidence interval between £194.98 and £264.86."
    )

    st.subheader("OLS Regression Insight")

    st.write(
        "The OLS model explained only 0.1% of price variation, indicating that Airbnb pricing is highly non-linear. "
        "This supports the use of tree-based machine learning models."
    )

# =========================
# Page 6: ML Model Insights
# =========================
elif page == "🤖 ML Model Insights":
    st.header("Machine Learning Model Insights")

    comparison = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Random Forest",
            "Gradient Boosting"
        ],
        "R²": [
            0.021,
            0.168,
            0.530
        ],
        "RMSE": [
            93813.98,
            86481.47,
            65011.86
        ],
        "MAE": [
            10055.51,
            5974.09,
            6745.94
        ]
    })

    st.subheader("Revenue Prediction Model Comparison")
    st.dataframe(comparison, use_container_width=True)

    fig = px.bar(
        comparison,
        x="Model",
        y="R²",
        title="Model Comparison by R² Score",
        text_auto=True
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Best Model")
    st.success("Gradient Boosting was selected as the best revenue prediction model with R² = 0.530.")

    st.subheader("Price Recommendation Model")
    st.info("Random Forest achieved R² = 0.578 and MAE = £55.70 for nightly price recommendation.")

    st.subheader("SHAP Explainability")
    shap_path = BASE_DIR / "reports/shap_summary.png"

    if shap_path.exists():
        st.image(str(shap_path), caption="SHAP Summary Plot - Revenue Prediction Model")
    else:
        st.warning("SHAP plot not found. Save it as reports/shap_summary.png to display it here.")

# =========================
# Page 7: Project Architecture
# =========================
elif page == "🧩 Project Architecture":
    st.header("Project Architecture")

    st.markdown("""
    ### End-to-End Workflow

    **Raw Data**
    - listings.csv
    - calendar.csv
    - reviews.csv
    - neighbourhoods.csv

    ↓

    **Data Engineering**
    - Ingestion
    - Profiling
    - Cleaning
    - Transformation
    - Validation

    ↓

    **Master Dataset**
    - listings + calendar + reviews + neighbourhoods
    - engineered features
    - revenue and occupancy metrics

    ↓

    **Analytics**
    - EDA
    - Statistical Analysis
    - SQL Data Modeling

    ↓

    **Machine Learning**
    - Revenue Prediction
    - Price Recommendation
    - SHAP Explainability

    ↓

    **Dashboard**
    - Executive Overview
    - Market Analytics
    - ML Prediction Tools
    - Statistical Insights
    """)

    st.success("This dashboard represents the final business-facing layer of the data engineering and analytics pipeline.")