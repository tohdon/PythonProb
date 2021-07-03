from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('WMT.csv', index_col = 'Date')
df.index = pd.to_datetime(df.index)
w = df.head()
print(w)
decomp = seasonal_decompose(df['Open'], freq=12)

fig = plt.figure()
fig = decomp.plot()
fig.set_size_inches(15, 8)
