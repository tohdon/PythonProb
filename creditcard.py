# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:54:05 2022

@author: Don
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.preprocessing import RobustScaler



data_path="C:\\software\\python\\diamond\\UCI_Credit_Card.csv"

default = pd.read_csv(data_path,index_col=0)
default.rename(columns=lambda x: x.lower(), inplace=True)
default.rename(columns={'pay_0':'pay_1','default.payment.next.month':'default'}, inplace=True)
default['grad_school'] = (default['education'] ==1).astype('int')
default['university'] = (default['education'] ==2).astype('int')
default['high_school'] = (default['education'] ==3).astype('int')

default['male'] = (default['sex']==1).astype('int')
default['married'] = (default['marriage']==1).astype('int')
default.drop(['sex','marriage','education'], axis=1, inplace=True)
pay_features = ['pay_' + str(i) for i in range(1,7)]
for p in pay_features:
    default[p] = (default[p] >0).astype(int)

print(default.head())
print(type(default))
target_name = 'default'
X = default.drop('default', axis=1)
feature_names = X.columns
robust_scaler = RobustScaler()
X = robust_scaler.fit_transform(X)
y = default[target_name]
print(y)
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.15, random_state=55, stratify=y)
print("=== TEST X===")
print(x_test)
print("==TRAIN X===")
print(x_train)

