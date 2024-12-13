"""Ко всем атрибутам можно добавить b и тогда работа будет с бинарными данными"""

'''
Открываем файл на чтение данных с помощью атрибута r и выводим их
with open('lorum.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
'''

'''
Открываем файл на чтение данных и дозапись с помощью атрибута r+ и выводим их
with open('lorum.txt', 'r+', encoding='utf-8') as file:
    data = file.read()
    print(data)
    file.write('New Note\n')
    data = file.read()
    print(data)
'''

'''
Открываем файл на запись данных с помощью атрибута w
with open('lorum.txt', 'w', encoding='utf-8') as file:
    file.write('New Note')
'''

'''
Открываем файл на запись данных, их можно считывать, стрибут w+
with open('lorum.txt', 'w+', encoding='utf-8') as file:
    file.write('New Note')
    file.seek(0)  # переносим в начало файла
    data = file.read()
    print(data)
'''
'''
Открываем файл на дозапись данных с помощью атрибута a
with open('lorum.txt', 'a', encoding='utf-8') as file:
    file.write('New Note')
'''
'''
Открываем файл на дозапись данных и чтение с помощью атрибута a+
with open('lorum.txt', 'a+', encoding='utf-8') as file:
    file.write('New Note\n')
    file.seek(0)  # переносим в начало файла
    data = file.read()
    print(data)
'''
