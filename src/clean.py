from pathlib import Path
import pandas as pd

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def clean_listings():

    listings = pd.read_csv(
        RAW_DATA_DIR / "listings.csv"
    )

    # Remove columns with 100% missing values
    columns_to_drop = [
        "license",
        "calendar_updated",
        "neighbourhood_group_cleansed"
    ]

    listings = listings.drop(
        columns=columns_to_drop,
        errors="ignore"
    )

    # Clean price column
    listings["price"] = (
        listings["price"]
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    listings["price"] = pd.to_numeric(
        listings["price"],
        errors="coerce"
    )

    PROCESSED_DATA_DIR.mkdir(
        exist_ok=True
    )

    listings.to_csv(
        PROCESSED_DATA_DIR /
        "listings_cleaned.csv",
        index=False
    )

    print("Cleaned listings saved successfully.")
    print(listings.shape)


if __name__ == "__main__":
    clean_listings()