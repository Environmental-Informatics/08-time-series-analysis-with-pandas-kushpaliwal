"""
Created on Mon Apr 19 2020

Author: kushpaliwal

Script to analyze daily discharge of Wabash river
"""

# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame, Panel

# Read data from given text file

inputdata = "WabashRiver_DailyDischarge_20150317-20160324.txt"

data = pd.read_table(inputdata,
                         header=None,
                         names=['agency','gauge_No','datetime','timezone','streamflow','remark'],
                         delimiter='\t',
                         skiprows=26)

# Convert timeseries data to a datetime format array

datetime = pd.to_datetime(data['datetime'])

flow = list(data['streamflow'])

streamflow = pd.DataFrame(flow,index=datetime,columns=['streamflow'])

# calculate daily mean streamflow

flow_daily = streamflow.resample('D').mean()

# plot of daily average streamflow

flow_daily.plot(figsize=(12,6))
plt.title("Daily Average Streamflow for Wabash River")
plt.legend(["Daily Mean"], loc='best',edgecolor='k')
plt.xlabel("Date")
plt.ylabel("Streamflow (cfs)")

plt.savefig("Daily Average Streamflow for Wabash River.pdf")

# extract the top 10 highest values 

flow_10d_max = flow_daily.nlargest(10,['streamflow'])
x = pd.to_datetime(flow_10d_max.index)

# plot of 10 days with highest streamflow

hydrograph=flow_daily.plot(figsize=(12,6))
topten=plt.scatter(x,flow_10d_max.streamflow,color='r',label='Top 10 Discharges')
hydrograph.legend(edgecolor='k')
plt.title('Top 10 Highest Daily Average Streamflow for Wabash River')
plt.xlabel('Date')
plt.ylabel('Streamflow (cfs)')
plt.savefig('10 Highest Discharge.pdf')
plt.show()

# calculate monthly mean streamflow

flow_monthly = streamflow.resample('M').mean()

# plot of monthly average streamflow

flow_monthly.plot(figsize=(12,6),style='D')
plt.title("Monthly Average Streamflow for Wabash River")
plt.legend(["Monthly Mean"], loc='best',edgecolor='k')
plt.xlabel("Date")
plt.ylabel("Streamflow (cfs)")

plt.savefig("Monthly Average Streamflow for Wabash River.pdf")