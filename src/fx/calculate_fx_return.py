import pandas as pd


def fx_returns_calculation():

    # File path to the cleaned FX price dataset
    path_input = "data/processed/fx_prices_clean.csv"

    # File path where the daily FX returns dataset will be saved
    path_output = "data/processed/fx_returns.csv"


    # Load cleaned FX prices into a pandas DataFrame
    df_fx = pd.read_csv(path_input)


    # Calculate daily FX returns while keeping the "Date" column unchanged
    df_fx.iloc[:, 1:] = df_fx.iloc[:, 1:].pct_change()


    # Save the FX returns dataset without the pandas index
    df_fx.to_csv(path_output, index=False)


    return df_fx