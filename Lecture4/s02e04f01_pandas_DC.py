# In this script we will start working more like data analysts
# using the python module pandas. Fetching data is done using build in functions to read csv and excel.

# Intro:
import pandas as pd
import numpy as np

# Lets create a Pandas Dataframe:
df = pd.DataFrame({'col one': [100, 200, 300], 'col two': [300, 400, 500]})

# Add a new column
df['test'] = [1, 2, 3]

# Choose data from a single column (Pandas Series)
df['col one']
df[['col one', 'col two']]  # note the double brackets in order to select multiple columns

# select columns using loc and iloc
df.loc[df['test'] == 3]
df.loc[df['test'] < 3, ['col one']]
df.loc[(df['test'] == 3) & (df['col one'] == 300)]  # multiple conditions (and).
df.loc[(df['test'] == 3) | (df['col one'] == 100)]  # multiple conditions (or).

# Get a single entry (could also be used for a range)
df.iloc[1, 2]

# Rename
df = df.rename({'col one': 'col_one', 'col two': 'col_two'}, axis='columns')

df.columns = ['col 1', 'col 2', 'col test']

df.add_prefix('X_')  # only works on columns for dataframes

# Create random data but now we name the columns
df_random = pd.DataFrame(np.random.rand(4, 8), columns=list('abcdefgh'))

# Exercise 1 - Load data from "Lecture4\data\excel_data.xlsx" into pandas.
# Investigate using the build in pandas functions (head, tail, describe). Google search for how to use them.
# Note that the resulting dataframe does not fit well into the console. Instead you can assign them to new variables.

# Try googling how to save a dataframe to excel, csv or pickle.
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_excel(r'Lecture4\data\excel_data.xlsx')
print(df.head(10))
print(df.tail())
df_describe = df.describe(include='all')  # here we add the info to a dataframe for better investigation

# Ad 1 - Use the function below to change the date and hour into datetime.
# Start by opening the datafile in excel to get an understanding of the data
# Plot the data from columns with "P_" in one plot (Price), "FB_" in another (flow) and make histograms of all the "P_" columns
# This can be done using either pure matplotlib or using the build in pandas plot and histogram functions
# Two and two - describe what is going on to each other?

# First we change the date sting to a datetime timestamp - Note that we need to add axis to the apply
df['DateTime'] = df.apply(lambda r: pd.to_datetime(r['Date'], format='%Y%m%d'), axis=1)
# Secondly we use datetime combine to add the timestamp and the hour as time
df['DateTime'] = df.apply(lambda r: dt.datetime.combine(r['DateTime'], dt.time(int(r['Hour']) - 1)), axis=1)

# Now we can set the datetime as index
df = df.set_index('DateTime')
df.drop(['Date', 'Hour'], axis=1, inplace=True)  # Notice the inplace!!
# This could also have been done with a chained command
# df = df.set_index('DateTime').drop(['Date', 'Hour'], axis=1)

# Lets plot the Price
plt.figure()
price_cols = [col for col in df.columns if 'P_' in col]
df[price_cols].plot()
plt.ylabel('Price [Euro]')
plt.show()

# Now do the same for the flow
# TODO: INSERT YOUR OWN CODE

# And plot histograms of the prices (hint: pandas has a build in function)
# (can you add more bins?)
# TODO: INSERT YOUR OWN CODE

# Exercise 2 - Data load gone wrong. Downloaded data has been split into multiple files.
# Build a DataFrame from multiple files.
# First make list with all the data paths
data_path = r'Lecture4/data/jan_split'
jan_files = ['{}/jan_{}.csv'.format(data_path, file) for file in
             ['Cons', 'Hourcet', 'Solar', 'ValueDate', 'Wind']]
# Then load them and combine them using pandas concat function
jan_data = pd.concat((pd.read_csv(file) for file in jan_files), axis='columns')
# Reorder the columns
jan_data = jan_data[['ValueDate', 'Hourcet', 'Cons', 'Wind', 'Solar']]

# Another way could be data monthly split. Now join all data from Lecture4/data/month_split/ into a dataframe called all_data
# into a file with some structure as jan_data but with data from the whole year (Make sure data is ordered by date and hour)
# hint: look up pandas sort_values() + reset_index
# hint: you can chain pandas commands by doing them followed by "."

# TODO: INSERT YOUR OWN CODE

# Notice that the ValueDate column contains strings. Change them to date objects
print("type(all_data['ValueDate'])", type(all_data['ValueDate'][0]))
# TODO: INSERT YOUR OWN CODE
print("type(all_data['ValueDate'])", type(all_data['ValueDate'][0]))


# Exercise 3 - Make a simple DA spot forecast. Use delta in residual load between d and d+1 to forecast spot
# First calculate the residual load (Cons-wind-solar)
# TODO: INSERT YOUR OWN CODE

# Ad 1 - add a spot. Use the following sql query to get the spot and merge onto all_data
import struct  # we need this build-in module to handle datatimeoffsets from a MSSQL database
import pyodbc  # this module from pypi is for connecting to a database
from datetime import datetime  # we can import specific types from a module, to avoid specifying the full name later

def handle_datetimeoffset(dto_value):
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 0, -6, 0)
    tweaked = [tup[i] // 100 if i == 6 else tup[i] for i in range(len(tup))]
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:06d} {:+03d}{:02d}".format(*tweaked)

# we need to specify our connection details
server = 'tcp:DKCLUDSQL02\INST102'
database = 'DPA_MarketData'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;Autocommit=True'

sql_query = """
    SELECT DateValueCET AS ValueDate, DATEPART(HOUR, ValueDateTimeOffset) + 1 AS Hourcet, PriceMWh
    FROM [DPA_MarketData].[dpv].[FactPowerSpotPriceActual]
    WHERE PowerPriceArea = 'Germany'
    AND DateValueCET BETWEEN '2019-01-01' AND '2020-01-01'
    AND DataSource = 'EPEX'
    AND Granularity = 'hour'
    ORDER BY ValueDateTimeOffset
        """

conn = pyodbc.connect(connection_string)
conn.add_output_converter(-155, handle_datetimeoffset)  # we do not use datetimes but added so that you remember this!
spot = pd.read_sql(sql_query, conn)
conn.close()

# Now use the pandas merge function to join all_data and spot
# TODO: INSERT YOUR OWN CODE

# Ad 2 - add a lagging residual and lagging spot + Calculate delta residual (Res - Res_lagging)
# Make a copy of the dataframe, shift dates 1 day ahead, rename prices and res.
# Now merge the two dataframes on ValueDate and Hourcet.
# hint: use pd.Timedelta()
all_data_lagging = all_data.copy()
# TODO: INSERT YOUR OWN CODE


# Ad 3 - Now make spot forecast as lagging_spot + delta_res * 1 euro/ 1000 mwh
# Display the result in a plot
# TODO: INSERT YOUR OWN CODE


# Ad 4 - Display a histogram with the error between the forecast and the spot
# TODO: INSERT YOUR OWN CODE

# AD 5 - Change from hourly profile to base (mean of the day)
# Hint look into pandas group by
# TODO: INSERT YOUR OWN CODE

# Bonus - Is there a correlation between what day og the week we have the large errors or on a specific price range?
