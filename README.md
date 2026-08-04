# FX Carry Trade Backtest

This project implements a quantitative backtest of a G10 FX carry trade strategy over the period from 2015 to 2025. Every quarter, the currencies are ranked by their 3-month interbank interest rates. The portfolio goes long the three currencies with the highest rates and short the three with the lowest rates.

## Results

<img width="1263" height="681" alt="image" src="https://github.com/user-attachments/assets/ee790fd1-5b3b-4a7a-93f8-3fe8894bb8c9" />




| Metric | Total Strategy | Carry Only | FX Movement Only |
|:-------|---------------:|-----------:|-----------------:|
| Annualized Return | 0.13% | ≈ 1.6% | ≈ -1.2% |
| Annualized Volatility | 8.31% | - | 8.32% |
| Sharpe Ratio | 0.02 | - | -0.15 |
| Max Drawdown | -15.4% | - | - |



*Volatility and the Sharpe ratio are not reported for the carry component because the model assumes a constant daily carry accrual. As a result, the isolated carry series has almost no variability, making these statistics uninformative.*




<img width="1085" height="422" alt="image" src="https://github.com/user-attachments/assets/16132b92-a0a6-4e3a-acf1-aef6dde1d955" />


## Key Finding

Breaking the strategy's return into its two components, carry and FX price movements, makes it clear where the overall performance came from. The interest rate carry delivered a steady cumulative gain of about 19.5% over the ten-year period. At the same time, exchange rate movements reduced returns by roughly 12.8% and were responsible for most of the volatility and drawdowns.

A large share of these losses came from a single event in January 2015. At that time, the strategy was short the Swiss franc (CHF). When the Swiss National Bank unexpectedly removed the EUR/CHF exchange rate floor, the franc appreciated by almost 20% in one day, causing a sharp loss.

This highlights one of the main risks of carry trading. Low-yielding currencies often act as safe-haven assets during periods of market stress. As a result, short positions in these currencies can experience sudden and significant losses, even when the overall strategy is performing as expected.


## Methodology
### Data

Quarterly 3-month interbank interest rates from the OECD were collected for AUD, CAD, CHF, EUR, GBP, JPY, NOK, NZD, and SEK against the USD. Daily FX spot prices were obtained from Yahoo Finance.

### Trading Signal

At the beginning of each quarter, all currencies are ranked by their interest rates. The strategy takes equally weighted long positions in the top three currencies and equally weighted short positions in the bottom three.

### Avoiding Look Ahead Bias

To keep the backtest realistic, interest rate data from quarter *t* is only used for trading in quarter *t+1*. This ensures that the strategy only uses information that would have been available at the time.

### Return Calculation

Daily portfolio returns combine two components. The first is the difference between the average FX return of the long positions and the average FX return of the short positions. The second is the daily interest rate carry, calculated from the annualized interest rate spread using the Actual/365 day count convention.

### Transaction Costs

The model assumes transaction costs of 1 basis point on the first trading day of each quarter to account for trading costs and slippage. In addition, a funding spread of 30 basis points per year is applied on a daily basis.


## Data Quality Notes

During validation, several unrealistic one-day price spikes were found in the Yahoo Finance data. These occurred on New Year's Day from 2019 to 2021 and on December 27, 2021. Since the prices returned to normal on the following trading day, they were treated as unreliable quotes caused by very low trading activity. These observations were corrected by carrying forward the last valid price.

Other large daily price movements were checked against independent historical sources. The moves in CHF (January 2015), GBP (June 2016), NOK (March 2020), and AUD (April 2025) matched real market events and were therefore left unchanged.


## Limitations
The backtest assumes that interest rate data is available for trading at the start of the following quarter, although actual publication delays are not included. Transaction costs are modeled as a fixed cost for each quarterly rebalance rather than for individual positions. 

The strategy itself follows a simple top three versus bottom three ranking. It does not include volatility scaling, momentum filters, or additional risk management techniques that are commonly used in professional trading to reduce exposure to events such as the 2015 Swiss franc shock.


## Project Structure
```
src/
├── rates/        # download, clean, and load OECD interest rate data
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


### The first execution downloads and cleans the raw data. Once the data has been processed, these steps can be commented out in main.py to speed up future runs.

### All charts and the final backtest return series are saved in data/processed/.
