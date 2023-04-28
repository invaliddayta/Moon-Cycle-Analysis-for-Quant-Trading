Moonphase Trading Backtest
This is a Python script that backtests the profitability of buying any given asset on new moon and selling at full moon over a given period. It utilizes Yahoo Finance API to retrieve historical price data and the ephem library to determine moon phase.

Usage
To run the program, simply provide the following arguments in the command line:

css
Copy code
python moonphase_trading.py [ticker] [interval] [start] [end] [-v]
ticker: The ticker symbol of the asset to be backtested (e.g. BTC-USD)
interval: The interval of historical price data to be retrieved (e.g. 1d for daily)
start: The start date of the backtesting period in the format yyyy-mm-dd
end: The end date of the backtesting period in the format yyyy-mm-dd
-v: Optional argument to display all trades taken in the given timeframe
Dependencies
This program requires the following libraries:

yfinance
pandas
ephem
argparse
You can install them via pip:

python
Copy code
pip install yfinance pandas ephem argparse
Example
Here's an example command to backtest Bitcoin (BTC-USD) trading on daily intervals from January 1, 2022 to April 1, 2022:

yaml
Copy code
python moonphase_trading.py BTC-USD 1d 2022-01-01 2022-04-01 -v
The program will output the cumulative ROI for the given period and, if the -v option is provided, all trades taken during the period.

Note
This is not an investment advice, and the program is for educational purposes only. Please consult a financial professional before making any investment decisions.
