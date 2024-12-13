import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

data = pd.read_csv('bikes.csv', encoding='utf-8', parse_dates=['Date'], dayfirst=True, index_col='Date')

'''
resample() переводит в процент какие-то числа, можно использовать с поиском медианных значение median()
'''

df = data['Berri 1'].resample('ME').median()
print(df)
df.plot(kind='bar')
plt.show()
