# In this script we will use a python module from pypi, pyodbc, to connect to a database and plot some charts with
# matplotlib

import struct  # we need this build-in module to handle datatimeoffsets from a MSSQL database
from statistics import mean

import pyodbc  # this module from pypi is for connecting to a database
from datetime import datetime  # we can import specific types from a module, to avoid specifying the full name later


# We need this to function to be able to read datetimeoffsets from a database. Datetimeoffsets are not natively
# supported by pyodbc
def handle_datetimeoffset(dto_value):
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 0, -6, 0)
    tweaked = [tup[i] // 100 if i == 6 else tup[i] for i in range(len(tup))]
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:06d} {:+03d}{:02d}".format(*tweaked)


# we need to specify our connection details
server = 'tcp:DKCLUDSQL02\INST102'
database = 'DPA_MarketData'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'

connection = pyodbc.connect(connection_string)  # open a connection to a database
# configure the connection to use the handle_datetimeoffset() function to understand datetimeoffsets
connection.add_output_converter(-155, handle_datetimeoffset)
cursor = connection.cursor()  # get a cursor object used to query the database

sql_query = """
SELECT PowerPriceArea, ValueDateTimeOffset, PriceMwh FROM [DPA_MarketData].[dpv].[FactPowerSpotPriceActual]
WHERE PowerPriceArea IN ('Germany', 'Austria')
AND Granularity = 'hour'
AND DataProvider = 'Danske Commodities'
AND DateValueCET BETWEEN '2019-01-01' AND '2020-01-01'"""


# get results one by one
cursor.execute(sql_query)
row = cursor.fetchone()
rows_one_by_one = []
while row:
    # uncomment one of below to see rows while they are processed
    #print(row)
    #print(f"PowerPriceArea={row[0]} ValueDateTimeOffset={row[1]} PriceMwh={row[2]}")
    # append row to `rows_one_by_one` with datetime parsed
    rows_one_by_one.append((row[0], datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f %z'), row[2]))
    row = cursor.fetchone()

print(f"We have fetched {len(rows_one_by_one)} rows")
print(f"rows[0]={rows_one_by_one[0]}")
print(f"rows[42]={rows_one_by_one[42]}")

# we can also fetch all results at once
cursor.execute(sql_query)  # execute the query again
rows_all = cursor.fetchall()  # get all rows

# we should be good citizens and close connections
cursor.close()
connection.close()

# import charting module
from matplotlib import pyplot

# lets sort our data
rows_one_by_one.sort(key=lambda x: x[1])
# and separate it into x/y axes
#x_axis = [x[1] for x in rows_one_by_one if x[0] == 'Germany']
#y_axis = [x[2] for x in rows_one_by_one if x[0] == 'Germany']

# using pyplot lets plot our data
#pyplot.plot(x_axis, y_axis, label='ger')
#pyplot.legend()  # tell pyplot to display a legend
#pyplot.show()  # display the chart

# Exercise 1 - add data for Austria to the chart.
# tip: how to add another data set to the chart?
# Call `pyplot.plot()` again with different data.
x_axis_1 = [x[1] for x in rows_one_by_one if x[0] == 'Germany']
y_axis_1 = [x[2] for x in rows_one_by_one if x[0] == 'Germany']
x_axis_2 = [x[1] for x in rows_one_by_one if x[0] == 'Austria']
y_axis_2 = [x[2] for x in rows_one_by_one if x[0] == 'Austria']
pyplot.plot(x_axis_1, y_axis_1, label='ger')
pyplot.plot(x_axis_2, y_axis_2, label='aus')
means_x = x_axis_1[6:]
means_y = [mean(y_axis_1[i-6:i+1]) for i in range(6, len(y_axis_1))]
pyplot.legend()  # tell pyplot to display a legend
pyplot.show()  # display the chart

# Exercise 2 - create a similar chart for power consumption for Germany and Switzerland.
# Use [DPA_MarketData].[dpv].[FactPowerConsumptionActual] table, 'Point Carbon' as data provider, use 'Hour'
# granularity, year 2019.
connection = pyodbc.connect(connection_string)
connection.add_output_converter(-155, handle_datetimeoffset)
cursor = connection.cursor()
sql_query = """
SELECT PowerPriceArea, ValueDateTimeOffset, VolumeMWh FROM [DPA_MarketData].[dpv].[FactPowerConsumptionActual]
WHERE PowerPriceArea IN ('Germany', 'Switzerland')
AND Granularity = 'hour'
AND DataProvider = 'Point Carbon'
AND DateValueCET BETWEEN '2019-01-01' AND '2019-12-31'"""
cursor.execute(sql_query)
rows_all = cursor.fetchall()
cursor.close()
connection.close()
rows_all = [(row[0], datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f %z'), row[2]) for row in rows_all]
rows_all.sort(key=lambda x: x[1])
x_axis_1 = [x[1] for x in rows_all if x[0] == 'Germany']
y_axis_1 = [x[2] for x in rows_all if x[0] == 'Germany']
x_axis_2 = [x[1] for x in rows_all if x[0] == 'Switzerland']
y_axis_2 = [x[2] for x in rows_all if x[0] == 'Switzerland']
pyplot.plot(x_axis_1, y_axis_1, label='Germany')
pyplot.plot(x_axis_2, y_axis_2, label='Switzerland')
pyplot.legend()
pyplot.show()


# Ad 1 - Display the same chart using logarithmic y scale. Googling "pyplot log scale" might help.
pyplot.plot(x_axis_1, y_axis_1, label='Germany')
pyplot.plot(x_axis_2, y_axis_2, label='Switzerland')
pyplot.legend()
pyplot.yscale("log")
pyplot.show()


# Ad 2 - Advanced - Compute a 30-days simple moving average (SMA) for Germany and Switzerland and add it to the chart.
# A SMA is the unweighted mean of the previous n data.
means_x_ger = x_axis_1[29:]
means_y_ger = [mean(y_axis_1[i-29:i+1]) for i in range(29, len(y_axis_1))]
means_x_aus = x_axis_2[29:]
means_y_aus = [mean(y_axis_2[i-29:i+1]) for i in range(29, len(y_axis_2))]
pyplot.plot(x_axis_1, y_axis_1, label='Germany')
pyplot.plot(x_axis_2, y_axis_2, label='Switzerland')
pyplot.plot(means_x_ger, means_y_ger, label='30-day moving average Germany')
pyplot.plot(means_x_aus, means_y_aus, label='30-day moving average Germany')
pyplot.legend()
pyplot.yscale("log")
pyplot.show()
