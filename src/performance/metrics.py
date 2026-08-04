import pandas as pd
import numpy as np


def equity_curve(returns):
    """Converts a series of daily returns into a cumulative equity curve
    starting at 1.0 (i.e. "1 euro invested")."""
    return (1 + returns).cumprod()


def annualized_return(returns, trading_days_per_year=252):
    total_return = (1 + returns).prod()
    n_years = len(returns) / trading_days_per_year
    return total_return ** (1 / n_years) - 1


def annualized_volatility(returns, trading_days_per_year=252):
    return returns.std() * np.sqrt(trading_days_per_year)#


def sharpe_ratio(returns, risk_free_rate=0.0, trading_days_per_year=252):
    excess_return = annualized_return(returns) - risk_free_rate
    vol = annualized_volatility(returns, trading_days_per_year)
    return excess_return / vol


def max_drawdown(returns):
    curve = equity_curve(returns)
    running_max = curve.cummax()
    drawdown = (curve - running_max) / running_max
    return drawdown.min()
