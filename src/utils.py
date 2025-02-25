"""Helper functions for 'back.ipynb'."""

import pandas as pd


def load_df(
    file_path: str = "./data/aapl.csv",
    from_date: str = "2008-01-01",
    req_cols: list[str] = [
        "datetime",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ],
) -> pd.DataFrame:
    """Load DataFrame and set 'Date' column as DatetimeIndex.

    Args:
        file_path (str):
            Absolute path to csv file (Default: "./data/aapl.csv").
        from_date (str):
            Date string ("YYYY-MM-DD") to start from (Default: "2008-01-01").
        req_cols (list[str]):
            List of required columns (Default: ["datetime", "open", "high", "low", "close", "volume"])

    Returns:
        df (pd.DataFrame): DataFrame with DatetimeIndex sorted in ascending order.
    """

    # Load DataFrame and format column headings (lowercase + replace white
    # space with underscore)
    df = pd.read_csv(file_path)
    df.columns = ["_".join(col.split()).lower() for col in df.columns]

    # Rename columns to suit backtrader and drop "adj_close" column
    df = df.rename(columns={"date": "datetime"})

    if "adj_close" in df.columns:
        df = df.drop(columns="adj_close")

    df = df.loc[:, req_cols]

    # Set 'Date' column as index and filter dates >= 'from_date'
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.set_index("datetime").sort_index(ascending=True)

    return df.loc[from_date:, :]
