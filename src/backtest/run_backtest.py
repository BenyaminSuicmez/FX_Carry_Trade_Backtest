import pandas as pd
from src.portfolio.build_portfolio import create_portfolio
from src.rates.clean_data import clean_rates


def backtest():

    wide_df = clean_rates()

    portfolio_df = create_portfolio(wide_df)

    # in progress, had to tackle topics covered in the upcoming commit
    # (=> data cleaning, found inconsistencies, documneted in README.md)
    