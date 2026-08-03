from src.clean_data import clean_rates
from src.portfolio.build_portfolio import create_portfolio
from src.fx.load_fx import load_fx_data
from src.fx.calculate_fx_return import fx_returns_calculation



wide_df = clean_rates()

portfolio_df = create_portfolio(wide_df)

fx_df = load_fx_data()


