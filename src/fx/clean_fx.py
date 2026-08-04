import pandas as pd


def clean_fx():

    # File path to the raw FX price data downloaded by "src/fx/download_fx.py"
    file_path_raw = "data/raw/fx_prices_raw.csv"

    # File path where the cleaned FX dataset will be saved
    path_clean_csv = "data/processed/fx_prices_clean.csv"


    # Load raw FX prices into a pandas DataFrame
    df = pd.read_csv(file_path_raw)

    # Convert to datetime to allow reliable date comparisons below
    df["Date"] = pd.to_datetime(df["Date"])


    # Known calendar days where Yahoo Finance reports unrealistic price
    # spikes that fully reverse on the next trading day (no real FX
    # trading happens on these dates, e.g. New Year's Day). Verified by
    # comparing daily returns against independent historical FX data.
    holidays_with_data_issues = pd.to_datetime([
            "2019-01-01",
            "2020-01-01",
            "2021-01-01",
            "2021-12-27",
    ])

    currency_columns = df.columns.drop("Date")

    # Shifted DataFrame: row i holds the value that was at row i-1,
    # i.e. "yesterday's price" for every date
    shifted = df[currency_columns].shift(1)

    # Forward-fill: replace the faulty price on each known holiday
    # with the previous trading day's price
    for holiday in holidays_with_data_issues:

        mask = df["Date"] == holiday

        df.loc[mask, currency_columns] = shifted.loc[mask, currency_columns]

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