# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:56:16 2021

@author: Don
"""
import scipy
import numpy as np  
import pandas as pd   
import matplotlib.pyplot as plt  
from scipy.stats import norm
%matplotlib inline
data = pd.read_csv(r'C:\software\python\MSFT.csv', index_col = 'Date')
log_returns = np.log(1 + data.pct_change())
print(log_returns.tail())

u = log_returns.mean()
var = log_returns.var()

print(str(var))
drift = u - (0.5 * var)
print("drift:" + str(drift))
stdev = log_returns.std()

print("Std dev:" + str(stdev))
np.array(drift)
print("drift values:" + str(drift.values))
#norm.ppf(0.95)
x = np.random.rand(10,2)

Z = norm.ppf(x)
print("random values: " + str(Z))
tinterval = 1000
iteration = 10
x1 = np.random.rand(tinterval,iteration)
print("daily return e (power r) where r= drift + std*z")
daily_returns = np.exp(drift.values + stdev.values*norm.ppf(x1))
print(daily_returns)

S0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = S0
print(S0)
for t in range(1, tinterval):
    price_list[t]= price_list[t-1] * daily_returns[t]
print(price_list)
plt.figure(figsize=(5,3))
plt.plot(price_list)

