from pathlib import Path
import pandas as pd


RAW_DATA_DIR = Path("data/raw")


def load_raw_data():
    """
    Load all raw Airbnb CSV files from data/raw folder.
    This is the ingestion stage of the pipeline.
    """
    listings = pd.read_csv(RAW_DATA_DIR / "listings.csv")
    calendar = pd.read_csv(RAW_DATA_DIR / "calendar.csv")
    reviews = pd.read_csv(RAW_DATA_DIR / "reviews.csv")
    neighbourhoods = pd.read_csv(RAW_DATA_DIR / "neighbourhoods.csv")

    return listings, calendar, reviews, neighbourhoods


if __name__ == "__main__":
    listings, calendar, reviews, neighbourhoods = load_raw_data()

    print("Raw data loaded successfully")
    print(f"Listings: {listings.shape}")
    print(f"Calendar: {calendar.shape}")
    print(f"Reviews: {reviews.shape}")
    print(f"Neighbourhoods: {neighbourhoods.shape}")