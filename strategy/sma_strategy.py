import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import connection_string
from sqlalchemy import create_engine

CONNECTION_STRING = connection_string
engine = create_engine(CONNECTION_STRING)

query = "SELECT * FROM stock_data WHERE instrument = 'HINDALCO' ORDER BY date"
data = pd.read_sql(query, engine)

data['SMA_50'] = data['close_price'].rolling(window=50).mean()
data['SMA_200'] = data['close_price'].rolling(window=200).mean()

data['Signal'] = 0

data.loc[50:, 'Signal'] = np.where(data.loc[50:, 'SMA_50'] > data.loc[50:, 'SMA_200'], 1, 0)

data['Position'] = data['Signal'].diff()

plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['close_price'], label='Close Price', alpha=0.5)
plt.plot(data['date'], data['SMA_50'], label='50-day SMA', alpha=0.75)
plt.plot(data['date'], data['SMA_200'], label='200-day SMA', alpha=0.75)

plt.plot(data[data['Position'] == 1]['date'], 
         data[data['Position'] == 1]['close_price'], 
         '^', markersize=10, color='g', label='Buy Signal')

plt.plot(data[data['Position'] == -1]['date'], 
         data[data['Position'] == -1]['close_price'], 
         'v', markersize=10, color='r', label='Sell Signal')

plt.title('SMA Crossover Strategy')
plt.legend()
plt.show()
