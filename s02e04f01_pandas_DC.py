# In this script we will start working more like data analysts
# using the python module pandas. Fetching data is done using build in functions to read csv and excel.
# Furthermore, we will use a in-house build package to fetch data (dcfoundation.MSSQL)

# Intro:
import pandas as pd
import numpy as np

# Lets create a Pandas Dataframe:
df = pd.DataFrame({'col one': [100, 200, 300], 'col two': [300, 400, 500]})

# Choose data from a single column (Pandas Series)
df['col one']

# Add a new column
df['test'] = [1, 2, 3]

# select columns using loc and iloc
df.loc[df['test'] == 3]
df.loc[df['test'] < 3, ['col one']]

df.iloc[1, 1]

# Rename
df = df.rename({'col one': 'col_one', 'col two': 'col_two'}, axis='columns')

df.columns = ['col 1', 'col 2', 'col test']

df.add_prefix('X_')

# Create random data but now we name the columns
df_random = pd.DataFrame(np.random.rand(4, 8), columns=list('abcdefgh'))


# Exercise 1 - Load data from "Lecture4\data\excel_data.xlsx" into pandas.
# Investigate using the build in pandas functions (head, tail, describe). Google search for how to use them
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_excel(r'Lecture4\data\excel_data.xlsx')
print(df.head())
print(df.tail())
df_describe = df.describe(include='all')

# Ad 1 - Use the function below to change the date and hour into datetime.
# Plot the data from columns with "P_" in one plot, "FB_" in another and make histograms of all the "P_" columns
# This can be done using either pure matplotlib or using the build in pandas plot and histogram functions
# (can you add more bins?)
# Can you describe what is going on?

df['DateTime'] = df.apply(lambda r: dt.datetime.combine(pd.to_datetime(r['Date'], format='%Y%m%d'),
                                                        dt.time(int(r['Hour'])-1)), axis=1)
df = df.set_index('DateTime')
df.drop(['Date', 'Hour'], axis=1, inplace=True)

plt.figure()
df[[col for col in df.columns if 'P_' in col]].plot()
plt.ylabel('Price [Euro]')
plt.show()

plt.figure()
df[[col for col in df.columns if 'FB_' in col]].plot()
plt.ylabel('Flow [Mwh]')
plt.show()

plt.figure()
df[[col for col in df.columns if 'P_' in col]].hist(bins=100)
plt.show()

# Exercise 2 - Data load gone wrong. Downloaded data has been split into multiple files.
# Build a DataFrame from multiple files.
from glob import glob
jan_files = sorted(glob(r'Lecture4/data/jan_split/jan_*.csv'))
jan_data = pd.concat((pd.read_csv(file) for file in jan_files), axis='columns')
jan_data = jan_data[['ValueDate', 'Hourcet', 'Cons', 'Wind', 'Solar']]

# Another way could be data monthly split. Now join all data from Lecture4/data/month_split/
# into a file with some structure as jan_data but with data from the whole year (Make sure data is ordered by date)
all_data = pd.DataFrame()

# Exercise 3 - Make a simple DA spot forecast. Use delta in residual load between d and d+1 to forecast spot
# First calculate the residual load (Cons-wind-solar)
all_data['Res'] = all_data['Cons'] - all_data['Wind'] - all_data['Solar']

# Ad 1 - add a spot. Use the following sql query to get the spot and merge onto all_data
from dcfoundation.MSSQL import Pandas as dcpd
sql_str = """
    SELECT DateValueCET AS ValueDate, DATEPART(HOUR, ValueDateTimeOffset) + 1 AS Hourcet, PriceMWh
    FROM [DPA_MarketData].[dpv].[FactPowerSpotPriceActual]
    WHERE PowerPriceArea = 'Germany'
    AND DateValueCET BETWEEN '2019-01-01' AND '2020-01-01'
    AND DataSource = 'EPEX'
    AND Granularity = 'hour'
    ORDER BY ValueDateTimeOffset
        """

connection_marketdata = dcpd.PandasDBConnectionManager(server_name='dpa_marketdata',
                                                        db_name='dpa_marketdata',
                                                        driver='ODBC Driver 17 for SQL Server')

spot = dcpd.PandasDBConnectionManager.read_query_to_df(connection_marketdata,
                                                                query_str=sql_str)




# Ad 2 - add a lagging residual  and lagging spot + Calculate delta residual
# Make a copy of the dataframe and shift dates 1 ahead. Now merge the two dataframes on ValueDate and Hourcet.



# Ad 3 - Now make spot forecast as lagging_spot - delta_res * 1 euro/ 10000 mwh
# Display the result in a plot


# Ad 4 - Display a histogram with the error between the forecast and the spot


# AD 5 - Change from hourly profile to base (mean of the day)
# Hint look into pandas group by


# Bonus - Is there a correlation between what day og the week we have the large errors or on a specific price range?


