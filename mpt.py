# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:37:21 2021

@author: Don
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

companies = ['WMT', 'FB']
df = pd.read_csv('C:\\software\\python\\WALMART_FB.csv', index_col='Date')
print(df)
df.index=pd.to_datetime(df.index)
(df / df.iloc[0] * 100).plot(figsize=(11, 6))
log_returns = np.log(df/ df.shift(1))
print(log_returns.head())
# Calculating Mean
lmean = log_returns.mean() * 250
#Calculating Covariance
lcov = log_returns.cov() * 250
#Calculating Correlation
lcorr = log_returns.corr()
num_assets = len(companies)
print("num assets " +str(num_assets))
weights = np.random.random(num_assets)
weights /= np.sum(weights)
print(weights)
np.sum(weights * log_returns.mean())* 250



# Expected Portfolio Variance
np.dot(weights.T,np.dot(log_returns.cov()* 250,weights))
# Expected Portfolio Volatility
np.sqrt(np.dot(weights.T,np.dot(log_returns.cov()* 250,weights)))
portfolio_returns=[]
portfolio_volatilities=[]
for x in range(1000):
    weights=np.random.random(num_assets)
    weights/=np.sum(weights)
    portfolio_returns.append(np.sum(weights*log_returns.mean())*250)
    portfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov(),weights))))
    
portfolio_returns,portfolio_volatilities

portfolio_returns=np.array(portfolio_returns)
portfolio_volatilities=np.array(portfolio_volatilities)
portfolio_returns,portfolio_volatilities

portfolios=pd.DataFrame({'Return': portfolio_returns,'Volatility':portfolio_volatilities})
print("portfolios")
print(portfolios.head())
portfolios.plot(x='Volatility',y='Return',kind='scatter',figsize=(10,6))
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')