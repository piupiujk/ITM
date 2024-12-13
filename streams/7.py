# Импортируем Pandas
import pandas as pd

# Считываем содержимое файла в переменную data:
data = pd.read_csv("bikes.csv")

print(data['Rachel1'].sum())
