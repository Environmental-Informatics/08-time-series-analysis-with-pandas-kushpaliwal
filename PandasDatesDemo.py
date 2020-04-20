"""
Created on Mon Apr 19 2020

Author: kushpaliwal

Codes from the tutorial, Time Series Analysis with Pandas, to study the time series datasets of Arctic Oscillation (AO) and North Atlantic Oscillation (NAO).

"""

# import necessary modules
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 15) # this limits maximum numbers of rows

# Check the version of pandas
print(pd.__version__)

# Get monthly AO data by ternimal prompt
# Read data
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')
print(ao[0:2]) 
print(ao.shape)

# Convert to time series data
dates = pd.date_range('1950-01',periods = ao.shape[0], freq='M')
print(dates)
print(dates.shape)

# Create first time series data
AO = Series(ao[:,2], index=dates)
print(AO)

# Plot AO data
AO.plot(title='Daily Atlantic Oscillation')
plt.show()
AO['1980':'1990'].plot()
plt.show()
AO['1980-05':'1981-03'].plot()
plt.show()

# Print some data
print(AO[120])
print(AO['1960-01'])
print(AO['1960'])
print(AO[AO>0])

# Craete another time series data
nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], dates_nao)
print(NAO.index)

# Create dataframe with both na and nao data
aonao = DataFrame({'AO': AO,'NAO': NAO})
aonao.plot(subplots=True)
plt.show()

# Output some data
print(aonao.head())
print(aonao['NAO'])
print(aonao.NAO)

# Add a column
aonao['Diff'] = aonao['AO'] - aonao['NAO']
print(aonao.head())

# Delete Diff column
del aonao['Diff']
print(aonao.tail())

print(aonao['1981-01':'1981-03'])

# Plot different combinations
import datetime
aonao.loc[(aonao.AO>0)&(aonao.NAO<0)
          & (aonao.index>datetime.datetime(1980,1,1))
          & (aonao.index<datetime.datetime(1989,1,1)),
          'NAO'].plot(kind='barh')
plt.show()

# Statistics
print(aonao.mean())
print(aonao.max())
print(aonao.min())
print(aonao.mean(1))
print(aonao.describe())

# Resampling
AO_mm = AO.resample('A').mean()
AO_mm.plot(style='g--')
plt.show()

# Median
AO_mm = AO.resample('A').median()
AO_mm.plot(title='Annual Median Values for AO')
plt.show()

# resample to 3 years
AO_mm = AO.resample('3A').apply(np.max)
AO_mm.plot()
plt.show()

# Specify several functions
AO_mm = AO.resample('A').apply(['mean',np.mean,np.max])
AO_mm['1900':'2020'].plot(subplots=True)
AO_mm['1900':'2020'].plot()
plt.show()
print(AO_mm)

# Rolling mean
aonao.rolling(window=12, center=False).mean().plot(style='-g', title=
             'Rolling mean for both AO and NAO')
plt.show()

# Rolling coorelation
aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g',title=
                'Rolling correlation')
plt.show()

print(aonao.corr())