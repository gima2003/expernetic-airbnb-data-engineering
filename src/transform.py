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

    print("Calendar loaded.")
    print(calendar.shape)

    print("Cleaning calendar price column...")

    # Works whether price is already numeric or text
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

    print("Transforming calendar data...")

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

    summary["estimated_revenue"] = (
        summary["booked_days"] * summary["avg_calendar_price"]
    )

    PROCESSED_DATA_DIR.mkdir(exist_ok=True)

    summary.to_csv(
        PROCESSED_DATA_DIR / "calendar_summary.csv",
        index=False
    )

    print("Calendar summary created successfully.")
    print(summary.shape)


if __name__ == "__main__":
    create_calendar_summary()