import pandas as pd


def clean_fx():

    # File path to the raw FX price data downloaded by "src/fx/download_fx.py"
    file_path_raw = "data/raw/fx_prices_raw.csv"

    # File path where the cleaned FX dataset will be saved
    path_clean_csv = "data/processed/fx_prices_clean.csv"


    # Load raw FX prices into a pandas DataFrame
    df = pd.read_csv(file_path_raw)


    # Currencies quoted as USD per currency unit need to be inverted
    inverse_currencies = [
        "CAD",
        "CHF",
        "JPY",
        "NOK",
        "SEK"
    ]


    # Convert all FX rates into the same USD-based direction
    for currency in inverse_currencies:
        df[currency] = 1 / df[currency]


    # Save the cleaned FX price dataset without the pandas index
    df.to_csv(path_clean_csv, index=False)


    return df