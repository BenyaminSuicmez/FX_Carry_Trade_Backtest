import pandas as pd
from src.portfolio.build_portfolio import create_portfolio
from src.rates.clean_data import clean_rates
from src.fx.load_fx_return import load_fx_returns


def backtest():

    wide_df = clean_rates()
    portfolio_df = create_portfolio(wide_df)

    fx_returns_df = load_fx_returns()

    # Assign each trading day to its calendar quarter
    fx_returns_df["quarter"] = fx_returns_df["Date"].dt.to_period("Q")

    # Cost assumptions
    transaction_costs = 0.00005      # 0.5 bp
    slippage = 0.00005               # 0.5 bp
    funding_spread = 0.003 / 365     # 30 bp per year

    daily_returns = []

    for _, row in portfolio_df.iterrows():

        trading_quarter = pd.Period(row["Trading Quarter"], freq="Q")

        days_in_quarter = fx_returns_df[
            fx_returns_df["quarter"] == trading_quarter
        ].copy()

        long_currencies = row["Long"]
        short_currencies = row["Short"]

        long_returns = days_in_quarter[long_currencies].mean(axis=1)
        short_returns = days_in_quarter[short_currencies].mean(axis=1)

        fx_return = long_returns - short_returns

        # Daily carry using Actual/365
        daily_carry = row["Annual Carry"] / 100 / 365

        # Gross return before costs
        gross_return = fx_return + daily_carry

        # Funding spread applies every day
        portfolio_return = gross_return - funding_spread

        # Transaction costs and slippage only on the first trading day
        if len(days_in_quarter) > 0:
            portfolio_return.iloc[0] -= (transaction_costs + slippage)

        quarter_result = pd.DataFrame({
            "Date": days_in_quarter["Date"],
            "FX Return": fx_return,
            "Carry Return": daily_carry,
            "Total Return": portfolio_return
        })

        daily_returns.append(quarter_result)


    daily_returns_df = pd.concat(daily_returns, ignore_index=True)

    daily_returns_df.to_csv("data/processed/backtest_returns.csv", index=False)

    return daily_returns_df