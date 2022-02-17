# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:54:05 2022

@author: Don
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import RobustScaler
from sklearn.neighbors import KNeighborsRegressor



data_path="C:\\software\\python\\diamond\\diamonds.csv"
diamonds = pd.read_csv(data_path)
print(diamonds.head(10))
print(diamonds['cut'].unique())
print(diamonds['color'].unique())
print(diamonds['clarity'].unique())
diamonds = pd.concat([diamonds, pd.get_dummies(diamonds['cut'],prefix='cut',drop_first=True)], axis=1)
diamonds = pd.concat([diamonds, pd.get_dummies(diamonds['color'],prefix='color',drop_first=True)], axis=1)

diamonds = pd.concat([diamonds, pd.get_dummies(diamonds['clarity'],prefix='clarity',drop_first=True)], axis=1)
diamonds.drop(['cut','clarity','color'], axis=1, inplace=True)
print(diamonds.head())
target_name ='price'
robust_scaler = RobustScaler()
X = diamonds.drop('price', axis=1)
feature_names = X.columns
X = robust_scaler.fit_transform(X)
y = diamonds[target_name]
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=55)
print("=== TEST X===")
print(x_test)
print("==TRAIN X===")
print(x_train)
models = pd.DataFrame(index=['train_mse','test_mse'],
                      columns=['KNN','Bagging', 'RandomForest','Boosting'])
knn = KNeighborsRegressor(n_neighbors=20, weights='distance', metric='euclidean', n_jobs=1)
knn.fit(x_train, y_train)
models.loc['train_mse','KNN'] = mean_squared_error(y_pred=knn.predict(x_train), y_true=y_train)
models.loc['test_mse','KNN'] = mean_squared_error(y_pred=knn.predict(x_test), y_true=y_test)
print("==models==")
print(models)

