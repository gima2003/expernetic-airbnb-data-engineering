from pathlib import Path
import pandas as pd

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def create_master_dataset():
    listings = pd.read_csv(PROCESSED_DATA_DIR / "listings_cleaned.csv")
    calendar = pd.read_csv(PROCESSED_DATA_DIR / "calendar_summary.csv")
    reviews = pd.read_csv(PROCESSED_DATA_DIR / "reviews_summary.csv")
    neighbourhoods = pd.read_csv(RAW_DATA_DIR / "neighbourhoods.csv")

    master = listings.merge(
        calendar,
        left_on="id",
        right_on="listing_id",
        how="left"
    )

    master = master.merge(
        reviews,
        left_on="id",
        right_on="listing_id",
        how="left",
        suffixes=("", "_reviews")
    )

    master = master.merge(
        neighbourhoods,
        left_on="neighbourhood_cleansed",
        right_on="neighbourhood",
        how="left"
    )

    master.to_csv(
        PROCESSED_DATA_DIR / "airbnb_master.csv",
        index=False
    )

    print("Master dataset created successfully.")
    print(master.shape)
    print("Columns:", master.shape[1])


if __name__ == "__main__":
    create_master_dataset()