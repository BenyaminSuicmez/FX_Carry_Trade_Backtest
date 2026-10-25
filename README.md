# FX Carry Trade Backtest

A backtest of a G10 FX carry trade from April 2015 to December 2025. Every quarter, the currencies are ranked by their 3-month interbank interest rates. The portfolio goes long the three currencies with the highest rates and short the three with the lowest.

## Results

<img width="1520" height="819" alt="image" src="https://github.com/user-attachments/assets/c88398b0-501a-4026-bb18-d54d105a154c" />




| Metric | Total Strategy | Carry Only | FX Movement Only |
|:-------|---------------:|-----------:|-----------------:|
| Annualized Return | 0.42% | ≈ 2.3% | ≈ -1.5% |
| Annualized Volatility | 6.48% | - | 6.49% |
| Sharpe Ratio | 0.07 | - | -0.23 |
| Max Drawdown | -15.0% | - | - |



*Volatility and Sharpe ratio are not reported for carry, since the daily carry is nearly constant.*


<img width="1512" height="588" alt="image" src="https://github.com/user-attachments/assets/fcb3574a-d95b-4c1b-8603-9e8c481fb4fa" />


## Key Finding

The interest rate carry earned about 28.5% in total, but exchange rate movements lost roughly 15.4% and caused most of the volatility and drawdowns.

The worst month was March 2020 (−6.0%). As markets sold off during the COVID-19 crisis, the high-yielding currencies the strategy was long (such as NOK, CAD and NZD) fell sharply, while low-yielding safe-haven currencies it was short (such as CHF and EUR) held up.

This shows the main risk of carry trading: sudden losses during market stress can erase years of accumulated carry.


## Methodology

**Data:** Quarterly 3-month interbank rates from the OECD for AUD, CAD, CHF, EUR, GBP, JPY, NOK, NZD and SEK. Daily FX spot prices against the USD from Yahoo Finance.

**Signal:** At the start of each quarter, currencies are ranked by interest rate. The strategy goes equally weighted long the top three and short the bottom three.

**No look-ahead bias:** Rates from quarter t are only used for trading in quarter t+1.

**Returns:** Daily return = average FX return of the longs minus the shorts, plus the daily carry from the interest rate spread (Actual/365, accrued over calendar days including weekends).

**Costs:** 1 basis point per quarterly rebalance for transaction costs and slippage, plus a funding spread of 30 basis points per year.


## Data Quality Notes

The Yahoo Finance data contained a few one-day price spikes that fully reversed the next day: on New Year's Day 2019–2021, on December 27, 2021, and on March 20, 2020 (USD/NOK reported at 7.74 between about 10.8 and 11.8). These were replaced with the previous day's price.

Other large moves in GBP (June 2016), NOK (March 2020) and AUD (April 2025) were checked against historical sources and match real market events.


## Limitations
- Publication delays of the interest rate data are ignored.
  
- Transaction costs are a flat cost per rebalance, not per position.
  
- No volatility scaling, momentum filters or other risk management, which professional strategies use to limit losses in events like March 2020.

## Project Structure
```
src/
├── rates/         # download, clean, and load OECD interest rate data
├── fx/            # download, clean, and load FX price/return data
├── portfolio/     # build quarterly long/short portfolios
├── backtest/      # combine signals and returns into a daily return series
└── performance/   # metrics (Sharpe, drawdown, ...) and charts
data/
├── raw/           # downloaded, unmodified data
└── processed/     # cleaned data, backtest results, charts
main.py            # runs the full pipeline
```

## How to Run
```bash
pip install -r requirements.txt
python main.py
```


The first run downloads and cleans the raw data. 
After that, these steps can be commented out in main.py. 
All charts and results are saved in data/processed/.
