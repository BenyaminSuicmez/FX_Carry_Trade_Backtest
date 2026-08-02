import pandas as pd


def create_portfolio(df_wide):

    # Initialize an empty list to store the portfolio composition of each quarter
    portfolio = []


    # Iterate over each quarter in the cleaned wide-format interest rate dataset
    # "_" is used because the row index is not needed
    for _, row in df_wide.iterrows():

        # Create a ranking of currencies by their interest rate for the current quarter
        # The quarter column is removed because it is not a currency
        # Higher interest rates are ranked first
        ranking = (
            row.drop("quarter")
                .astype(float)
                .sort_values(ascending=False)
        )


        # Select the three currencies with the highest interest rates as the long portfolio
        long = ranking.head(3)

        # Select the three currencies with the lowest interest rates as the short portfolio
        short = ranking.tail(3)


        # Store the portfolio decision and corresponding carry information for this quarter
        portfolio.append({
            "Quarter": row["quarter"],

            # Store currency names instead of the complete Series
            "Long": long.index.tolist(),
            "Short": short.index.tolist(),

            # Calculate the equally weighted average interest rate of each side
            "Long-Rate": long.mean(),
            "Short-Rate": short.mean(),

            # Calculate the theoretical carry advantage of the strategy (p.a.)
            "Annual Carry": long.mean() - short.mean()
        })


    # Convert the list of quarterly portfolios into a DataFrame for further analysis
    return pd.DataFrame(portfolio)