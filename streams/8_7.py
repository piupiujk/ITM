import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

data = pd.read_csv('bikes.csv', encoding='utf-8')
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

print(data['Date'])
