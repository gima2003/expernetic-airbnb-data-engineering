from pathlib import Path
import pandas as pd

PROCESSED_DATA_DIR = Path("data/processed")


def validate_listings():

    listings = pd.read_csv(
        PROCESSED_DATA_DIR / "listings_cleaned.csv"
    )

    print("\nVALIDATION RESULTS")
    print("=" * 50)

    # Negative prices
    negative_prices = (
        listings["price"] < 0
    ).sum()

    print(
        f"Negative prices: {negative_prices}"
    )

    # Negative bedrooms
    if "bedrooms" in listings.columns:

        negative_bedrooms = (
            listings["bedrooms"] < 0
        ).sum()

        print(
            f"Negative bedrooms: {negative_bedrooms}"
        )

    # Negative bathrooms
    if "bathrooms" in listings.columns:

        negative_bathrooms = (
            listings["bathrooms"] < 0
        ).sum()

        print(
            f"Negative bathrooms: {negative_bathrooms}"
        )

    # Duplicate IDs
    duplicate_ids = (
        listings["id"]
        .duplicated()
        .sum()
    )

    print(
        f"Duplicate Listing IDs: {duplicate_ids}"
    )


if __name__ == "__main__":
    validate_listings()