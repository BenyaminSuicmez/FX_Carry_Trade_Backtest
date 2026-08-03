import pandas as pd


def create_portfolio(df_wide):

    # Initialize an empty list to store the quarterly portfolio decisions
    portfolio = []


    # Define the last available FX trading quarter
    max_trading_quarter = pd.Period(
        "2025Q4",
        freq="Q"
    )


    # Iterate over each quarter in the cleaned wide-format interest rate dataset
    for _, row in df_wide.iterrows():

        # Convert signal quarter into pandas Period format
        signal_quarter = pd.Period(
            row["quarter"],
            freq="Q"
        )


        # Portfolio is traded in the following quarter
        trading_quarter = signal_quarter + 1


        # Skip signals where no FX return data is available
        if trading_quarter > max_trading_quarter:
            continue


        # Rank currencies by their interest rate
        # Higher interest rates are ranked first
        ranking = (
            row.drop("quarter")
               .astype(float)
               .sort_values(ascending=False)
        )


        # Select three highest-yielding currencies as long positions
        long = ranking.head(3)


        # Select three lowest-yielding currencies as short positions
        short = ranking.tail(3)


        # Store portfolio decision and carry characteristics
        portfolio.append({

            # Quarter where the information was observed
            "Signal Quarter": str(signal_quarter),

            # Quarter where the portfolio is actually traded
            "Trading Quarter": str(trading_quarter),

            # Currency composition
            "Long": long.index.tolist(),
            "Short": short.index.tolist(),

            # Interest rate characteristics
            "Long-Rate": long.mean(),
            "Short-Rate": short.mean(),

            # Expected annual carry spread
            "Annual Carry": long.mean() - short.mean()
        })


    # Convert portfolio list into DataFrame
    portfolio_df = pd.DataFrame(portfolio)


    return portfolio_df