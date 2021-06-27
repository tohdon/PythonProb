import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('WMT.csv', index_col='Date')
df.index = pd.to_datetime(df.index)
print(df.head())