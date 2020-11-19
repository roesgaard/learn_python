# In this script we will start working more like data analysts
# using the python module pandas. Fetching data is done using build in functions to read csv and excel.
# Furthermore, we will use a in-house build package to fetch data (dcfoundation.MSSQL)

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
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_excel(r'Lecture4\data\excel_data.xlsx')
print(df.head(10))
print(df.tail())
df_describe = df.describe(include='all')  # here we add the info to a dataframe for better investigation

# Ad 1 - Use the function below to change the date and hour into datetime.
# Start by opening the datafile in excel to get an understanding of the data
# Plot the data from columns with "P_" in one plot, "FB_" in another and make histograms of all the "P_" columns
# This can be done using either pure matplotlib or using the build in pandas plot and histogram functions
# Two and two - describe what is going on to each other?

# First we change the date sting to a datetime timestamp - Note that we need to add axis to the apply
df['DateTime'] = df.apply(lambda r: pd.to_datetime(r['Date'], format='%Y%m%d'), axis=1)
# Secondly we use datetime combine to add the timestamp and the hour as time
df['DateTime'] = df.apply(lambda r: dt.datetime.combine(r['DateTime'], dt.time(int(r['Hour']) - 1)), axis=1)

# Now we can set the datetime as index
df = df.set_index('DateTime')
df.drop(['Date', 'Hour'], axis=1, inplace=True)  # Notice the inplace!!

# Lets plot the Price
plt.figure()
price_cols = [col for col in df.columns if 'P_' in col]
df[price_cols].plot()
plt.ylabel('Price [Euro]')
plt.show()

# Now do the same for the flow
plt.figure()
df[[col for col in df.columns if 'FB_' in col]].plot()
plt.ylabel('Flow [Mwh]')
plt.show()

# And plot histograms of the prices (hint: pandas has a build in function)
# (can you add more bins?)
plt.figure()
df[[col for col in df.columns if 'P_' in col]].hist(bins=100)
plt.show()


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
all_data = [r'Lecture4/data/month_split/{}_data.csv'.format(file) for file in range(1, 13)]
all_data = pd.concat((pd.read_csv(file) for file in all_data), axis='rows')
all_data = all_data[['ValueDate', 'Hourcet', 'Cons', 'Wind', 'Solar']].sort_values(by=['ValueDate', 'Hourcet']).reset_index(drop=True)

# Notice that the ValueDate column contains strings. Change them to date objects
print('type(my_sincerity)', type(all_data['ValueDate'][0]))
all_data['ValueDate'] = pd.to_datetime(all_data['ValueDate']).dt.date
print('type(my_sincerity)', type(all_data['ValueDate'][0]))


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

# Now use the pandas merge function to join all_data and spot
all_data = all_data.merge(spot, on=['ValueDate', 'Hourcet'])

# Ad 2 - add a lagging residual and lagging spot + Calculate delta residual (Res - Res_lagging)
# Make a copy of the dataframe, shift dates 1 day ahead, rename prices and res.
# Now merge the two dataframes on ValueDate and Hourcet.
# hint: use pd.Timedelta()
all_data_lagging = all_data.copy()
all_data_lagging['ValueDate'] = all_data_lagging['ValueDate'] + pd.Timedelta(days=1)
all_data_lagging.rename({'Res': 'Res_Lagging', 'PriceMWh': 'PriceMWh_Lagging'}, axis='columns', inplace=True)

all_data = all_data.merge(all_data_lagging[['ValueDate', 'Hourcet', 'Res_Lagging', 'PriceMWh_Lagging']],
                          on=['ValueDate', 'Hourcet'])

all_data['res_delta'] = all_data['Res'] - all_data['Res_Lagging']
all_data = all_data.sort_values(by=['ValueDate', 'Hourcet'])


# Ad 3 - Now make spot forecast as lagging_spot - delta_res * 1 euro/ 1000 mwh
# Display the result in a plot
all_data['price_delta'] = all_data['PriceMWh_Lagging'] + all_data['res_delta'] / 1000

all_data[['PriceMWh', 'forecast']].plot()
plt.show()

# Ad 4 - Display a histogram with the error between the forecast and the spot
all_data['error'] = all_data['PriceMWh'] - all_data['forecast']
all_data['error'].hist(bins=100)
plt.show()

# AD 5 - Change from hourly profile to base (mean of the day)
# Hint look into pandas group by
base = all_data.groupby('ValueDate').mean()
base['error'].hist(bins=100)
plt.show()

# Bonus - Is there a correlation between what day og the week we have the large errors or on a specific price range?
