import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="London Airbnb Intelligence Dashboard",
    page_icon="🏠",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/airbnb_featured.csv")

@st.cache_resource
def load_models():
    revenue_model = joblib.load("models/revenue_predictor.pkl")
    price_model = joblib.load("models/price_recommender.pkl")
    return revenue_model, price_model

data = load_data()
revenue_model, price_model = load_models()

st.markdown("""
<style>
.main-title {
    font-size: 44px;
    font-weight: 800;
}
.subtitle {
    font-size: 18px;
    color: #9ca3af;
}
.card {
    padding: 22px;
    border-radius: 16px;
    background-color: #111827;
    border: 1px solid #374151;
}
.result-box {
    padding: 28px;
    border-radius: 18px;
    background-color: #064e3b;
    border: 1px solid #10b981;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🏠 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "EDA Insights",
        "Revenue Predictor",
        "Price Recommender",
        "Project Summary"
    ]
)

st.markdown('<div class="main-title">London Airbnb Market Intelligence Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Data Engineering • Analytics • Statistics • Machine Learning</div>', unsafe_allow_html=True)
st.divider()

if page == "Overview":
    st.header("Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Listings", f"{data.shape[0]:,}")
    col2.metric("Average Price", f"£{data['price'].mean():.2f}")
    col3.metric("Average Occupancy", f"{data['occupancy_rate'].mean():.2f}%")
    col4.metric("Average Revenue", f"£{data['estimated_revenue_l365d'].mean():.2f}")

    st.subheader("Dataset Preview")
    st.dataframe(data.head(20), use_container_width=True)

elif page == "EDA Insights":
    st.header("EDA Insights")

    st.subheader("Listings by Room Type")
    st.bar_chart(data["room_type"].value_counts())

    st.subheader("Top 10 Boroughs by Listings")
    st.bar_chart(data["neighbourhood_cleansed"].value_counts().head(10))

    st.subheader("Top 10 Boroughs by Average Price")
    avg_price = (
        data.groupby("neighbourhood_cleansed")["price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(avg_price)

elif page == "Revenue Predictor":
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
            review_scores_rating = st.number_input("Review Rating", min_value=0.0, max_value=5.0, value=4.8)
            occupancy_rate = st.number_input("Occupancy Rate (%)", min_value=0.0, max_value=100.0, value=60.0)
            number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=25)
            review_text_count = st.number_input("Review Text Count", min_value=0, value=25)

        with col3:
            avg_review_length = st.number_input("Average Review Length", min_value=0.0, value=250.0)
            host_experience_years = st.number_input("Host Experience Years", min_value=0.0, value=3.0)
            room_type = st.selectbox("Room Type", sorted(data["room_type"].dropna().unique()))
            neighbourhood = st.selectbox("Borough", sorted(data["neighbourhood_cleansed"].dropna().unique()))
            host_is_superhost = st.selectbox("Superhost", ["t", "f"])

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

elif page == "Price Recommender":
    st.header("Price Recommendation Model")
    st.info("This section will be connected next.")

elif page == "Project Summary":
    st.header("Project Summary")

    st.success("Project includes Data Engineering, EDA, Statistical Analysis, SQLite Data Modeling, and Machine Learning.")

    st.write("""
    Completed components:
    - Data ingestion and cleaning pipeline
    - Master Airbnb dataset
    - Feature engineering
    - SQLite star schema
    - Statistical hypothesis testing
    - Revenue prediction model
    - Price recommendation model
    - Streamlit dashboard
    """)