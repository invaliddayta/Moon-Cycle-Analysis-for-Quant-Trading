<h1>Moonphase Trading Backtest</h1>
<h2>Description</h2>
<p>Moonphase Trading Backtest is a Python script that backtests the profitability of buying any given asset on new moon and selling at full moon over a given period. It utilizes Yahoo Finance API to retrieve historical price data and the ephem library to determine moon phase.</p>

<h2>Features</h2>

- Easy to use command-line interface
- Historical data retrieval for multiple intervals
- Moon phase calculation using ephem library
- Detailed logging of all trades taken during the period

<h2>Installation</h2>
<p>To use Moonphase Trading Backtest, you need to have Python 3 installed on your system. You also need to install the required dependencies. To install the dependencies, run the following command in your terminal:</p>

```
pip install yfinance pandas ephem argparse
```

<h2>Usage</h2>
<p>To run the program, simply provide the following arguments in the command line:</p>

```
python moonphase_trading.py [ticker] [interval] [start] [end] [-v]
```
- `ticker`: The ticker symbol of the asset to be backtested (e.g. BTC-USD)
- `interval`: The interval of historical price data to be retrieved (e.g. 1d for daily)
- `start`: The start date of the backtesting period in the format yyyy-mm-dd
- `end`: The end date of the backtesting period in the format yyyy-mm-dd
- `-v`: Optional argument to display all trades taken in the given timeframe

<h2>Dependencies</h2>
<p>This program requires the following libraries:</p>

- `yfinance`
- `pandas`
- `ephem`
- `argparse`
<p>You can install them via pip:</p>

```
pip install yfinance pandas ephem argparse
```
<h2>Example</h2>
<p>Here's an example command to backtest Bitcoin (BTC-USD) trading on daily intervals from January 1, 2022 to April 1, 2022:</p>

```
python moonphase_trading.py BTC-USD 1d 2022-01-01 2022-04-01 -v
```
The program will output the cumulative ROI for the given period and, if the -v option is provided, all trades taken during the period.

<h2>Note</h2>
<p>This is not an investment advice, and the program is for educational purposes only. Please consult a financial professional before making any investment decisions.</p>
