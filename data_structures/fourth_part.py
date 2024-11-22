# 4 ЧАСТЬ
# 1 задача
digits = [1, 2, 3, 4, 5]
print(digits[0])
print(digits[2])
print(digits[0:3])

# 2 задача
city = ['Ростов', '+', 'на', '-', 'Дону']
city[1] = '-'
print(city[0] + city[1] + city[2] + city[3] + city[4])

# 3 задача
dig_and_str = ['a', 's', '1', 'a', '32', '23']
digits = []
strings = []
for el in dig_and_str:
    try:
        digits.append(int(el))
    except:
        strings.append(el)
print(digits)
print(strings)

# 4 задача
del strings[-1]
print(strings[::-1])

# 5 задача
set_dig_and_str = set(dig_and_str)
print(set_dig_and_str)
# set хранит в себе элементы в одном экземпляре, поэтому буква 'a', которая потвотралсь, осталась только одна
