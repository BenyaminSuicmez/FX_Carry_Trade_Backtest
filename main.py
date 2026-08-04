from src.rates.download_rates import download
from src.rates.clean_data import clean_rates
from src.fx.download_fx import download_fx_data
from src.fx.clean_fx import clean_fx
from src.rates.load_rates import load_interest_rates
from src.portfolio.build_portfolio import create_portfolio
from src.fx.calculate_fx_return import fx_returns_calculation
from src.backtest.run_backtest import backtest


# Download the OECD 3-month interest rate data.
# After running this once, the data is stored locally.
# You can then comment out download().

# download()


# Clean and format the downloaded interest rate data.
# After running this once, you can comment it out as well.

# clean_rates()


# Download raw FX price data from Yahoo Finance.
# After running this once, the data is stored locally.
# You can then comment out download_fx_data().

# download_fx_data()


# Clean and format the downloaded FX price data.
# After running this once, you can comment it out as well.

# clean_fx()


# Load the cleaned interest rate dataset
wide_df = load_interest_rates()

# Create the quarterly long/short portfolios
portfolio_df = create_portfolio(wide_df)

# Calculate daily FX returns
fx_returns_df = fx_returns_calculation()

# Run the carry trade backtest
backtest()