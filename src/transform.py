from pathlib import Path
import pandas as pd

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def create_calendar_summary():
    print("Loading calendar data...")

    calendar = pd.read_csv(
        RAW_DATA_DIR / "calendar.csv",
        usecols=["listing_id", "available", "price"]
    )

    calendar["price"] = (
        calendar["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    calendar["price"] = pd.to_numeric(
        calendar["price"],
        errors="coerce"
    )

    summary = (
        calendar
        .groupby("listing_id")
        .agg(
            available_days=("available", lambda x: (x == "t").sum()),
            booked_days=("available", lambda x: (x == "f").sum()),
            total_calendar_days=("available", "count"),
            avg_calendar_price=("price", "mean")
        )
        .reset_index()
    )

    summary["occupancy_rate"] = (
        summary["booked_days"] / summary["total_calendar_days"]
    ) * 100

    PROCESSED_DATA_DIR.mkdir(exist_ok=True)

    summary.to_csv(
        PROCESSED_DATA_DIR / "calendar_summary.csv",
        index=False
    )

    print("Calendar summary created.")
    print(summary.shape)


def create_reviews_summary():
    print("Loading reviews data...")

    reviews = pd.read_csv(
        RAW_DATA_DIR / "reviews.csv",
        usecols=["listing_id", "date", "comments"]
    )

    reviews["date"] = pd.to_datetime(
        reviews["date"],
        errors="coerce"
    )

    reviews["comment_length"] = (
        reviews["comments"]
        .fillna("")
        .astype(str)
        .str.len()
    )

    summary = (
        reviews
        .groupby("listing_id")
        .agg(
            review_text_count=("comments", "count"),
            first_review_date=("date", "min"),
            last_review_date=("date", "max"),
            avg_review_length=("comment_length", "mean")
        )
        .reset_index()
    )

    summary.to_csv(
        PROCESSED_DATA_DIR / "reviews_summary.csv",
        index=False
    )

    print("Reviews summary created.")
    print(summary.shape)


if __name__ == "__main__":
    create_calendar_summary()
    create_reviews_summary()