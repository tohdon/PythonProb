# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:14:17 2021

@author: Don
"""
import pandas as pd
import quandl

appl = pd.read_csv('C:\\software\\python\\AAPL.csv',index_col='Date', parse_dates=True)
amzn = pd.read_csv('C:\\software\\python\\AMZN.csv',index_col='Date', parse_dates=True)
csco = pd.read_csv('C:\\software\\python\\CSCO.csv',index_col='Date', parse_dates=True)
ibm = pd.read_csv('C:\\software\\python\\IBM.csv',index_col='Date', parse_dates=True)

for df_stock in [appl, amzn, csco, ibm]:
    df_stock['Normalize Return'] = df_stock['Adj Close']/df_stock.iloc[0]['Adj Close']
    
print(appl.head())


for df_stock,allocate in zip([appl, amzn, csco, ibm],[.3,.2,.4,.1]):
    df_stock['allocation'] = df_stock['Normalize Return']*allocate
    
for df_stock,allocate in zip([appl, amzn, csco, ibm],[.3,.2,.4,.1]):
    df_stock['Position Values'] = df_stock['allocation']*10000
print(appl.head())

portfolio_val = pd.concat([appl['Position Values'],csco['Position Values'],ibm['Position Values'], amzn['Position Values']],axis=1)
portfolio_val.columns =['APP PosL','CSCO PosL','IBM PosL','AMZN PosL']
print(portfolio_val)
