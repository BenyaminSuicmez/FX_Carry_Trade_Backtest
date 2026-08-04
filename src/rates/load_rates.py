import pandas as pd


def load_interest_rates():

    # Load the cleaned interest rate data
    rates_df = pd.read_csv("data/processed/oecd_rates_clean.csv")


    return rates_df