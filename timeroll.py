import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('WMT.csv', index_col='Date',parse_dates=True)
#df['Open'].plot()
df['Close'].expanding(min_periods=1).mean().plot(figsize=(16,5))
