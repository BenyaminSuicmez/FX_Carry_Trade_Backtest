from src.rates.clean_data import clean_rates
from src.portfolio.build_portfolio import create_portfolio
from src.fx.calculate_fx_return import fx_returns_calculation


wide_df = clean_rates()

portfolio_df = create_portfolio(wide_df)

fx_returns = fx_returns_calculation()



print(portfolio_df.head())
print(portfolio_df.tail())