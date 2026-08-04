import pandas as pd


def load_fx_prices():

    # Load the processed FX price dataset
    fx_df = pd.read_csv("data/processed/fx_prices_clean.csv")

    return fx_df