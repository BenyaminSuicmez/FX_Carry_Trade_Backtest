import pandas as pd


def clean_rates():

    # File path to the raw CSV data downloaded by "src/download_rates.py"
    file_path = "data/raw/oecd_ir3tib_2015_2025.csv"


    # File path where the cleaned dataset will be saved
    path_clean_csv = "data/processed/oecd_rates_clean.csv"


    # Load raw data into a pandas DataFrame
    df = pd.read_csv(file_path) 


    # Keep only the columns required for the backtest
    df_clean = df[["REF_AREA", "TIME_PERIOD", "OBS_VALUE"]] 


    # Rename columns for readability
    df_clean = df_clean.rename(columns={
        "REF_AREA": "currency",
        "TIME_PERIOD": "quarter",
        "OBS_VALUE": "rate"
    })


    # Rename the EA20 area code to EUR for consistency with currency notation
    df_clean["currency"] = df_clean["currency"].replace("EA20", "EUR")


    # Create a temporary date column to enable chronological sorting by quarter
    df_clean["quarter_date"] = pd.PeriodIndex(
        df_clean["quarter"],
        freq="Q"
    )


    # Sort by currency and then chronologically within each currency
    df_clean = df_clean.sort_values(
        by=["currency", "quarter_date"]
    )


    # Remove the temporary sorting column
    df_clean = df_clean.drop(columns="quarter_date")


    # Transform the dataset from long format into wide format
    df_wide = df_clean.pivot(
        index="quarter",
        columns="currency",
        values="rate"
    )


    # Reset index to convert quarter back into a regular column
    df_wide = df_wide.reset_index()


    # Save the cleaned dataset without the pandas index
    df_wide.to_csv(path_clean_csv, index=False)

    return df_wide