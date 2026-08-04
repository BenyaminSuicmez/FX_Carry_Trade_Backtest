import matplotlib.pyplot as plt
from src.performance.metrics import equity_curve


def plot_equity_curve(dates, total_returns, carry_returns, fx_returns,
                       output_path="data/processed/equity_curve.png",
                       initial_capital=1000):

    equity_total = initial_capital * equity_curve(total_returns)
    equity_carry = initial_capital * equity_curve(carry_returns)
    equity_fx = initial_capital * equity_curve(fx_returns)

    plt.figure(figsize=(12, 6))
    plt.plot(dates, equity_total, label="Total Strategy", linewidth=2)
    plt.plot(dates, equity_carry, label="Carry Only", linestyle="--")
    plt.plot(dates, equity_fx, label="FX Movement Only", linestyle="--")

    plt.title("FX Carry Trade — Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.legend()
    plt.grid(True)

    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()

def plot_drawdown(dates, total_returns, output_path="data/processed/drawdown.png"):

    curve = equity_curve(total_returns)
    running_max = curve.cummax()
    drawdown = (curve - running_max) / running_max

    plt.figure(figsize=(12, 4))
    plt.fill_between(dates, drawdown * 100, 0, color="firebrick", alpha=0.5)
    plt.plot(dates, drawdown * 100, color="firebrick", linewidth=0.8)

    plt.title("FX Carry Trade — Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown (%)")
    plt.grid(True)

    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()