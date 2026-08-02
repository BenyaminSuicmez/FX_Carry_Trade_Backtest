from src.clean_data import clean_rates
from src.portfolio.build_portfolio import create_portfolio
from src.fx.load_fx import load_fx_data




df_wide = clean_rates()

portfolio_df = create_portfolio(df_wide)

fx_df = load_fx_data()

