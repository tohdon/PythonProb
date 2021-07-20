# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 08:30:45 2021

@author: Don
"""

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

start = '2020-1-1'
end ='2021-1-1'
TSLA = wb.DataReader("TSLA", 'stooq', start, end)
print(TSLA)

print("READ TESLA CSV")
HIST_TSLA = pd.read_csv(r'C:\software\python\TSLA.csv', index_col='Date')
print(HIST_TSLA)

HIST_TSLA['simple_return'] = (HIST_TSLA['Close']/HIST_TSLA['Close'].shift(1))-1 
print(HIST_TSLA['simple_return'].head(10))
HIST_TSLA.index = pd.to_datetime(HIST_TSLA.index)
HIST_TSLA['simple_return'].plot(figsize = (9,5))
plt.show()

print("TESLA AVERAGE RETURN")
TSLA_average_return = HIST_TSLA['simple_return'].mean()
print(TSLA_average_return)

print("TESLA AVERAGE ANNUAL RETURN")
TSLA_annual_average_return = HIST_TSLA['simple_return'].mean()*250
print(str(TSLA_annual_average_return*100)+'%')