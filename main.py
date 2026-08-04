from src.rates.download_rates import download
from src.rates.clean_data import clean_rates
from src.fx.download_fx import download_fx_data
from src.fx.clean_fx import clean_fx
from src.fx.calculate_fx_return import fx_returns_calculation
from src.portfolio.build_portfolio import create_portfolio
from src.backtest.run_backtest import backtest


result = backtest()
print(result.head())
print(result["Carry Return"].describe())