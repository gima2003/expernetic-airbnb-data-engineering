from pathlib import Path
import pandas as pd

PROCESSED_DATA_DIR = Path("data/processed")


def create_master_dataset():

    listings = pd.read_csv(
        PROCESSED_DATA_DIR / "listings_cleaned.csv"
    )

    calendar = pd.read_csv(
        PROCESSED_DATA_DIR / "calendar_summary.csv"
    )

    master = listings.merge(
        calendar,
        left_on="id",
        right_on="listing_id",
        how="left"
    )

    master.to_csv(
        PROCESSED_DATA_DIR /
        "airbnb_master.csv",
        index=False
    )

    print("Master dataset created successfully.")
    print(master.shape)


if __name__ == "__main__":
    create_master_dataset()