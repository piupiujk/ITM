import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

data = pd.read_csv('bikes.csv')
print(data[['Maisonneuve 1', 'Maisonneuve 2']])
counts = data['Maisonneuve 1'].value_counts()
counts.plot(kind='bar')
plt.show()
