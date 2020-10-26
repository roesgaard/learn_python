# https://nbviewer.jupyter.org/github/justmarkham/pandas-videos/blob/master/top_25_pandas_tricks.ipynb

import pandas as pd
import numpy as np

df = pd.DataFrame({'col one':[100, 200], 'col two':[300, 400]})

df['col one']

df['test'] = [1,2]

df_random = pd.DataFrame(np.random.rand(20, 30))

pd.DataFrame(np.random.rand(4, 8), columns=list('abcdefgh'))

# Rename
df = df.rename({'col one':'col_one', 'col two':'col_two'}, axis='columns')

df.columns = ['col_one', 'col_two']

df.add_prefix('X_')

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head() # default value = 5
drinks.tail()
drinks.describe()

drinks.sort_values(by='beer_servings', ascending=False).head()


# Select columns by data type
drinks.dtypes

drinks.select_dtypes(include='number').head()

drinks.select_dtypes(include=['number', 'object', 'category', 'datetime']).head()

drinks.select_dtypes(exclude='number').head()


# select columns using loc and iloc
drinks.loc[drinks['beer_servings']> 100]
drinks.loc[drinks['beer_servings']> 100, ['country', 'beer_servings']]

drinks.loc[(drinks['beer_servings']> 100) & (drinks['total_litres_of_pure_alcohol']> 10)]

drinks.iloc[5]

# Build a DataFrame from multiple files (row-wise)
pd.read_csv('data/stocks1.csv')

from glob import glob
stock_files = sorted(glob('data/stocks*.csv'))
stock_files
stocks = pd.concat((pd.read_csv(file) for file in stock_files))
stocks = pd.concat((pd.read_csv(file) for file in stock_files), ignore_index=True)


#Build a DataFrame from multiple files (column-wise)
drink_files = sorted(glob('data/drinks*.csv'))
drinks_new = pd.concat((pd.read_csv(file) for file in drink_files), axis='columns')

# Aggregate by multiple functions
drinks[drinks.continent == 'Europe'].beer_servings.sum()
drinks.groupby('continent').beer_servings.sum()

drinks.groupby('continent').beer_servings.agg(['sum','count','mean','min','max'])


# apply
# Use the stocks df from earlier
import datetime as dt
stocks = pd.read_csv('http://bit.ly/smallstocks') # We do not use parse_dates=['Date']
type(stocks['Date'][0])
type(dt.datetime.strptime(stocks['Date'][0],'%Y-%m-%d'))
stocks['Date_apply'] = stocks['Date'].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d'))
type(stocks['Date_apply'][0])

# alternative way:
stocks['Date_dt'] =  pd.to_datetime(stocks['Date'], format='%Y-%m-%d')
type(stocks['Date_dt'][0])


# sql
from dcfoundation.MSSQL import Pandas as dcpd

sql_str = """
            SELECT TOP 10 * 
            FROM dpv.FactHydroActual
          
            """
connection_marketdata = dcpd.PandasDBConnectionManager(server_name='DPA_MarketData',
                                                        db_name='DPA_MarketData',
                                                        driver='ODBC Driver 17 for SQL Server')

flow_power = dcpd.PandasDBConnectionManager.read_query_to_df(connection_marketdata,
                                                                query_str=sql_str)

flow_power.describe(include='all')


# excel
df = pd.read_excel ('data\excel_data.xlsx', sheet_name='temp')
print(df)
df.describe(include='all')

df['DateTime'] = df.apply(lambda r : pd.datetime.combine(pd.to_datetime(r['Date'], format='%Y%m%d'),dt.time(int(r['Hour'])-1)),axis=1)
df = df.set_index('DateTime')
df.drop(['Date','Hour'], axis=1, inplace=True)
df[[col for col in df.columns if 'P_' in col]].plot()
df[[col for col in df.columns if 'FB_' in col]].plot()


df[[col for col in df.columns if 'FB_' in col]].hist(bins=100)
