from pathlib import Path
import pandas as pd

RAW_DATA_DIR = Path("data/raw")


def profile_dataframe(df, name):

    print(f"\n{'='*60}")
    print(f"DATASET: {name}")
    print(f"{'='*60}")

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    profile_report = pd.DataFrame({
        "column": df.columns,
        "dtype": df.dtypes.astype(str),
        "missing_count": df.isnull().sum(),
        "missing_pct": round(df.isnull().mean()*100,2),
        "unique_values": df.nunique()
    })

    profile_report = profile_report.sort_values(
        by="missing_count",
        ascending=False
    )

    print("\nTop 10 Missing Values")
    print(profile_report.head(10))

    return profile_report


if __name__ == "__main__":

    listings = pd.read_csv(RAW_DATA_DIR / "listings.csv")

    report = profile_dataframe(listings, "LISTINGS")

    report.to_csv(
        "reports/listings_profile_report.csv",
        index=False
    )

    print("\nProfile report saved successfully.")