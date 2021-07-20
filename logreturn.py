# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 08:30:45 2021

@author: Don
"""
import numpy as np
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


print("READ TESLA CSV")
HIST_TSLA = pd.read_csv(r'C:\software\python\TSLA.csv', index_col='Date')
print(HIST_TSLA)

HIST_TSLA['log_return'] = np.log(HIST_TSLA['Close']/HIST_TSLA['Close'].shift(1))-1 
print(HIST_TSLA['log_return'].head(10))

HIST_TSLA.index = pd.to_datetime(HIST_TSLA.index)
HIST_TSLA['log_return'].plot(figsize = (8,5))
plt.show()

print("TESLA LOG AVERAGE RETURN")
TSLA_log_return = HIST_TSLA['log_return'].mean()
print(TSLA_log_return)

print("TESLA AVERAGE ANNUAL RETURN")
TSLA_annu_log_return = HIST_TSLA['log_return'].mean()*250
print(str(TSLA_annu_log_return*100)+'%')