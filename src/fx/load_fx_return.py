import pandas as pd


def load_fx_returns():

    # Load the processed FX-returns dataset
    fx_df = pd.read_csv("data/processed/fx_returns.csv")

    # Convert to datetime to allow filtering by quarter/date range later
    fx_df["Date"] = pd.to_datetime(fx_df["Date"])

    return fx_df