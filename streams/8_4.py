import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

data = pd.read_csv('bikes.csv', encoding='utf-8', index_col='Date')


dfs = [data[['Berri 1', 'Maisonneuve 1']], data[['Berri 1', 'Maisonneuve 1']]]
new_df = pd.concat(dfs, axis=1)
print(new_df[:5])
