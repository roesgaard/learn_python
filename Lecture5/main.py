import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Setup how pandas is displayed in the console
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

"""
Please go through the exercises before visiting the website.

This lecture is taken from
https://mitchellrosenthalofficial.medium.com/crash-course-python-pandas-for-trading-and-investing-part-1-714b77dfdc21

All credit goes to the author.
"""


# In this script we will work more with Pandas and plotting.
# We will simulate a random stock price, and try to make a simple trading strategy.

# First a dataframe with date index is created
PERIODS = 365*2
our_index = pd.date_range(start='2021-01-01', periods=PERIODS, freq='D')
df = pd.DataFrame(index=our_index)
print('Header of dataframe')
print(df.head())

"""-----Exercise 1 - Create the 'stock prices'-----"""
# Create a column called 'Close' that is filled with small number drown from a normal distribution
# (use numpy - random- normal) Set loc=0.0002 and scale=0.011. What should size be?
df['Close'] = INSERT CODE
# Now calculate the exponential for each value in 'Close'.
# This is equal to e^N and will be 1 plus % change for that day.
df['Close'] = INSERT CODE
# Set the first value to 1 (at location 0). This correspond to setting starting value to 100%
INSERT CODE
# Finally take the cumulative product of the column (cumprod). Does you understand what this does?
df['Close'] = INSERT CODE
# now plot our Fake stock price. (try to include the 'legend')
df[['Close']].plot(figsize=(7, 5), title='Our Fake Stock Price')

"""-----Exercise 2 - Calculate a moving average-----"""
# Often when analysing stocks a moving average is used to smooth the data and show an overall trend.
# Create a column called '100MA' containing the 100 day moving average and plot it together with the data.
# Hint: use google or ctrl+click the link: https://letmegooglethat.com/?q=calculate+moving+average+pandas+stackoverflow
df['100MA'] = INSERT CODE
df[['Close', '100MA']].plot(figsize=(7, 5), title='Our Fake Stock Price')
# For later use we will not calculate the simple indicator 'Distance from Moving Average':
# https://school.stockcharts.com/doku.php?id=technical_indicators:distance_from_ma
df['100MAdist'] = INSERT CODE

# Now we can plot the two dataset together in two subplots.
# Using this function it is possible to join more plots into one figure.
# If you cannot follow the logic behind it please google or ask instructor.
"""
f1 = plt.figure(figsize=(7, 5))
ax1 = f1.add_subplot(2, 1, 1)
ax2 = f1.add_subplot(2, 1, 2)
df[[XXX]].plot(title='XXX', ax=ax1)
df['YYY'].plot(title='YYY', ax=ax2)
plt.tight_layout()
plt.show()
"""


f2 = plt.figure(figsize=(7, 5))
ax1 = f2.add_subplot(2, 1, 1)
ax2 = f2.add_subplot(2, 1, 2)
INSERT CODE
INSERT CODE
plt.tight_layout()
plt.show()

"""-----Exercise 3 - Working with signals-----"""
# A simple trading strategy is to stay invested when the stock price is above the moving average.
# To indicate this we will create a column called 'MAsignal' with 1 when close is above 100MA and 0 otherwise.
# This is best done using np.where(condition, true_value, false_value)
df['MAsignal'] = INSERT CODE

# From this list we want the dates where the condition is true (df['MAsignal'] == 1).
# Where this is true take the index and put them into a list called true_dates
# Hint: dfFiltered = df[SomeConditionHere] + .index + .tolist()
true_dates = INSERT CODE

# Use the below code to plot the  stock data with highlighted periods where close > 100MA
f3 = plt.figure(figsize=(9, 6))
ax1 = f3.add_subplot(1, 1, 1)
df[['Close', '100MA']].plot(title='Our Fake Stock Price', ax=ax1)
for x in true_dates:
    ax1.axvline(x, color='tab:green', alpha=0.27, linewidth=.25,   linestyle='-')

# another solution to make the plot with highlighted signal is to make two different curves:
# SignalTrue: should be Closing price if Close > 100MA, otherwise np.NaN
# SignalFalse: should be Closing price if Close < 100MA, otherwise np.NaN
df['SignalTrue'] = INSERT CODE
df['SignalFalse'] = INSERT CODE

# Plot using the following command:
f4 = plt.figure(figsize=(9, 6))
ax1 = f4.add_subplot(1, 1, 1)
df[['SignalTrue', 'SignalFalse']].plot(title='Our Fake Stock Price', ax=ax1)
plt.show()


"""-----Exercise 4 - Making OHLC data-----"""
# Our signal is based on the daily close.
# If we want to take any action on this signal we would normally take the action on the next day open.
# To do so we will try to generate prices in 30 minute increments, filter the "marked open hours"
# and resample the data to OHLC date (open, high, low, close)

# Create our index to have same number of days and multiply with 24 hours/day and 2 half hours for each hour.
# Note that we have chosen freq='30T' which equals 30 minutes
# First we make sure that we do not mistakenly use the old dataframe
df = None
our_index_half_hour = pd.date_range(start='2020-12-21', periods=PERIODS*24*2, freq='30T')
df_ohlc = INSERT CODE

# In order to generate a curve with similar gains as previous we will have to reduce the mean change.
# From the source of this exercise the idea is:
"""
Next, I generate random, small decimal numbers that represent the logarithm of my 30-minute returns.
But what should the mean and stdev of the random distribution be?
Earlier, we set the mean change from the end of the previous day to the end of the current day to be (0.0002).
Since we are making higher-frequency data, we need to reduce this mean % change to preserve the original rate of growth.
Recall that there are 48 30-minute increments per day.
The new % change, called R, relates to the old one (r) in this formula:
(1+R)⁴⁸ = (1+r)¹
(1+R) = (1+r)^(1/48)
R = [(1+r)^(1/48)]-1
What about stdev? For stocks that follow a random walk, the variance of their returns is directly proportional to time.
Standard deviation is the square root of variance, so it is proportional to the square root of time.
So the new stdev (STDEV) is related to the old one (stdev) like so:
(STDEV)/(sqrt(1/48)) = (stdev)/(sqrt(1))
STDEV = (stdev)(sqrt(1))(sqrt(1/48))
"""
# Use this to create the new stock price series and add it to our dataframe df_ohlc
R_old = INSERT CODE
Stdev_old = INSERT CODE
R_new = INSERT CODE
Stdev_new = INSERT CODE
df_ohlc['Close'] = np.random.normal(loc=R_new, scale=Stdev_new, size=PERIODS*24*2)
df_ohlc['Close'] = INSERT CODE
df_ohlc['Close'] INSERT CODE
df_ohlc['Close'] = INSERT CODE
df_ohlc['Close'].plot(figsize=(7, 5))
plt.show()

# Second step was to filter the data to only keep changes in the "open" hours
# and afterwards use the pandas function resample('1D').ohlc on the closing price.
# We will also change the naming to capital letter since this is the usual for Stock data

df_ohlc = df_ohlc.between_time('09:30', '16:00')
df_ohlc = INSERT CODE
df_ohlc.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'}, inplace=True)
df_ohlc.head()

# If we want to plot the candlesticks or verify that we have proper OHLC data we can use the following.
# However, this does not work with to much data since it is not possible to observe the candles.
import mplfinance as mpf
mpf.plot(df_ohlc[-50:], type='candle')


"""-----Exercise 5 - Betting on the strategy-----"""
# The strategy is to be in the marked when the close is above the 100MA and out when it is below.
# The buy/sell transaction should occur when the signal is flipping from 0 to 1 or the other way.

# For each day there are 4 potential changes to our portfolio:
"""
1. If the signal equaled 1 at the end of yesterday’s close, and 0 the day before, then today we buy at the open.
        Today, we experience the change from the open to the close.
2. If the signal equaled 1 at the end of yesterday’s close and the day before, we continue to hold through today.
        We experience the change from yesterday’s close to today’s close.
3. If the signal equaled 0 at the end of yesterday’s close and 1 the day before, then today we exit (sell) at the open.
        Today, we experience the change from yesterday’s close to today’s open. This is the overnight change.
4. If the signal equaled 0 at the end of yesterday’s close and 0 the day before,
        we do nothing today and experience no change. This is our default setting.
"""
# First we create the two columns '100MA' and 'MAsignal' similar to the first part.
df_ohlc['100MA'] = INSERT CODE
df_ohlc['MAsignal'] = INSERT CODE

# now we translate the 3 first changes into conditions. Notice that shift(1) will take the datapoint one step earlier.
condition1 = (df_ohlc['MAsignal'].shift(1) == 1) & (df_ohlc['MAsignal'].shift(2) == 0)
condition2 = INSERT CODE
condition3 = INSERT CODE

# Now we will create a column 'PortChng' that will be 0 as default (condition 4),
# but will have the relevant changes where the different conditons are fulfilled.
df_ohlc['PortChng'] = INSERT CODE
df_ohlc['PortChng'] = INSERT CODE
df_ohlc['PortChng'] = INSERT CODE
df_ohlc['PortChng'] = INSERT CODE

# In order to get the accumulated change in portfolio we will have to add 1 to 'PortChng' and use cumprod.
df_ohlc['Port'] = INSERT CODE
df_ohlc['Port'] = INSERT CODE

f6 = plt.figure(figsize=(9, 6))
ax1 = f6.add_subplot(1, 1, 1)
true_indexvals = df_ohlc[condition1 | condition2 | condition3].index.tolist()
df_ohlc[['Close', 'Port']].plot(title='Testing the 100MA Strategy', ax=ax1)
for x in true_indexvals:
    ax1.axvline(x, color='tab:green', alpha=0.50, linewidth=.25, linestyle='-')
ax1.legend(loc='upper left')
plt.show()

# Notice that the port change = 0 when we are out of strategy.


"""-----Exercise Bonus - Slippage-----"""
# The next natural step is to consider slippage.
# I will not go through this, but I do recommend you to visit the source of this exercise if you want to look into it.
# if you are restricted by access please reach out to SRD

# Furthermore, one could start looking into actual stock prices. to download these for pandas one solution is to use:
# datafile = 'SPY.csv'
# data = pd.read_csv(datafile, index_col = 'Date')
# data.index = pd.to_datetime(data.index) # Converting the dates from string to datetime format