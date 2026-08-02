import yfinance as yf
import pandas as pd


def download_fx_data():

    # File path where the raw FX price data will be saved
    path_fx_raw = "data/raw/fx_prices_raw.csv"


    # Dictionary to store downloaded FX price series
    fx_data = {}


    # Yahoo Finance ticker symbols for the selected FX universe
    fx_tickers = {
        "AUD": "AUDUSD=X",
        "CAD": "USDCAD=X",
        "CHF": "USDCHF=X",
        "EUR": "EURUSD=X",
        "GBP": "GBPUSD=X",
        "JPY": "USDJPY=X",
        "NOK": "USDNOK=X",
        "NZD": "NZDUSD=X",
        "SEK": "USDSEK=X"
    }


    # Download daily FX close prices for each currency
    for currency, ticker in fx_tickers.items():

        data = yf.download(
            ticker,
            start="2015-01-01",
            end="2026-01-01"
        )

        # Extract the closing price series
        close = data["Close"].squeeze()

        # Store the price series under the currency name
        fx_data[currency] = close


    # Combine all currency series into one DataFrame
    fx_df = pd.DataFrame(fx_data)


    # Save raw FX prices locally
    fx_df.to_csv(path_fx_raw)


    return fx_df