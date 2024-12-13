import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

data = pd.read_csv('bikes.csv', encoding='utf-8', parse_dates=['Date'], dayfirst=True, index_col='Date')
# parse_dates - Перевод столбец который указываем в формат datetime

rachel1 = data[['Rachel1']].copy()
rachel1.loc[:, 'weekday'] = rachel1.index.weekday

weekday_counts = rachel1.groupby('weekday').sum()
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')

plt.show()
