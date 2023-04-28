import yfinance as yf
import pandas as pd
import ephem
import argparse

# read the user arguments
parser = argparse.ArgumentParser(
    description='A trading program that that backtests the profitability of buying any given asset on new moon and selling at full moon over a given period')
parser.add_argument("ticker", help="1) Argument Ticker: provide the Ticker eg. BTC-USD")
parser.add_argument("interval", help="2) Give a Interval that should be Tested eg. 1d")
parser.add_argument("start", help="3) Input a Date from which to start in format: yyyy-mm-dd")
parser.add_argument("end", help="4) Input a Date to end in format: yyyy-mm-dd")
parser.add_argument("-v", "--verbose", help="5) A char or number outputs all trades taken in the given timeframe",
                    default=None)
args = parser.parse_args()

print("Backtesting Moonphase profitability of", args.ticker, "on the", args.interval, "timeframe from", args.start,
      "to", args.end, "...")

# Get the historical BTC price
btc = yf.Ticker(args.ticker)
df = btc.history(start=args.start, end=args.end, interval=args.interval)

# Convert date column to datetime format
df['Date'] = pd.to_datetime(df.index)

# Initialize arrays to store full moon and new moon prices
full_moon_close = []
new_moon_close = []

# Initialize arrays mark where a buy/sell occurred
date_open = []
date_close = []

# Initializing variables for calculating the position
position_open = False
cumulative_ROI = 0
profit = 0

# Iterate through each row in the dataframe
for index, row in df.iterrows():
    date = row['Date']
    close_price = row['Open']

    # Use ephem library to determine moon phase
    moon = ephem.Moon()
    moon.compute(date)
    phase = moon.moon_phase

    # Check if phase is full moon or new moon
    if phase > 0.99 and position_open == 0:
        full_moon_close.append(close_price)
        date_open.append(date)
        position_open = True



    elif (phase < 0.01) and (position_open) == 1:
        new_moon_close.append(close_price)
        date_close.append(date)
        position_open = False

# iterate through data rows and calculate ROI, profit and ROI
for i in range(len(new_moon_close)):
    profit = profit - full_moon_close[i] + new_moon_close[i]
    ROI = ((new_moon_close[i] / full_moon_close[i]) - 1) * 100
    cumulative_ROI = cumulative_ROI + ROI
    real_return = - full_moon_close[i] + new_moon_close[i]
    if args.verbose is not None:
        print("Open:", full_moon_close[i], "Date:", date_open[i], "Close:", new_moon_close[i], "Date:", date_close[i],  "R/R", real_return, "ROI:", ROI, "%")

print("ROI", cumulative_ROI, "%")
