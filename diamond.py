import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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



