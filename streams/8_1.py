import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

data = pd.read_csv('bikes.csv')
data['Rachel1'].plot()
data.plot()


plt.show()
