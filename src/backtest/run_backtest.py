import pandas as pd
from src.portfolio.build_portfolio import create_portfolio
from src.rates.clean_data import clean_rates
from src.fx.load_fx_return import load_fx_returns


def backtest():

    wide_df = clean_rates()
    portfolio_df = create_portfolio(wide_df)

    fx_returns_df = load_fx_returns()

    # Assign each trading day to its calendar quarter, so we can
    # match it against the "Trading Quarter" in portfolio_df
    fx_returns_df["quarter"] = fx_returns_df["Date"].dt.to_period("Q")

    # Collect daily portfolio returns across all quarters
    daily_returns = []

    for _, row in portfolio_df.iterrows():

        trading_quarter = pd.Period(row["Trading Quarter"], freq="Q")

        days_in_quarter = fx_returns_df[fx_returns_df["quarter"] == trading_quarter]

        long_currencies = row["Long"]
        short_currencies = row["Short"]

        long_returns = days_in_quarter[long_currencies].mean(axis=1)
        short_returns = days_in_quarter[short_currencies].mean(axis=1)

        fx_return = long_returns - short_returns

        # Convert the annualized carry into a daily amount using an
        # Actual/365 day-count convention
        daily_carry = row["Annual Carry"] / 100 / 365

        # Total daily portfolio return combines FX movement and carry
        portfolio_return = fx_return + daily_carry

        quarter_result = pd.DataFrame({
            "Date": days_in_quarter["Date"],
            "FX Return": fx_return,
            "Carry Return": daily_carry,
            "Total Return": portfolio_return
        })

        daily_returns.append(quarter_result)

    # Combine all quarters into one continuous daily return series
    daily_returns_df = pd.concat(daily_returns, ignore_index=True)

    return daily_returns_df