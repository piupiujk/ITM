import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

data = pd.read_csv('bikes.csv', encoding='utf-8', parse_dates=['Date'], dayfirst=True, index_col='Date')

print(data['Cute-Sainte-Catherine'].unique())

data['Cute-Sainte-Catherine'] = data['Cute-Sainte-Catherine'].replace(0, np.nan)
print(data['Cute-Sainte-Catherine'].unique())


data['Cute-Sainte-Catherine'] = data['Cute-Sainte-Catherine'].fillna(0)
print(data['Cute-Sainte-Catherine'].unique())

