# 5 ЧАСТЬ
# 1 задача
people = {
    'name': 'Александр',
    'age': 22,
    'sex': 'male',
    'height': 173,
    'weight': 60,
}

# 2 задача
print('Имя:', people['name'])
print('Возраст:', people['age'])
print('Пол:', people['sex'])
print('Рост:', people['height'])
print('Вес:', people['weight'])

# 3 задача
people['foot_size'] = 43
print(people)

# 4 задача
del people['age']
print(people)
