# 2 ЧАСТЬ
# 1 задача
l = 238  # сантимеры
l_m = l // 100  # метры
print('Метры:', l_m)

# 2 задача
m = 3422  # кг
m_t = m // 1000  # тонна
print('Тонн:', m_t)

# 3 задача
b = 2048  # байты
kb = b // 1024
print('Килобайты:', kb)

# 4 задача
a = 14
b = 7
b_in_a = a // b
print('Количество b в a:', b_in_a)

# 5 задача
a = 19
b = 10
b_in_a_ost = a % b
print('Оставшаяся часть:', b_in_a_ost)

# 6 задача
a = 89
first_digit = a // 10
second_digit = a % 10
print('Первое число:', first_digit)
print('Второе чило:', second_digit)

# 7 задача
a = 45
first_digit = a // 10
second_digit = a % 10
print('Сумма цифр числа:', first_digit + second_digit)
print('Произведение цифр числа:', first_digit * second_digit)

# 8 задача
a = 73
first_digit = a // 10
second_digit = a % 10
b = int(str(second_digit) + str(first_digit))
print('Новое число:', b)

# 9 задача
a = 421
first_digit = a // 100
print('Первая цифра числа:', first_digit)

# 10 задача
a = 478
second_digit = (a // 10) % 10
last_digit = a % 10
print('Вторая цифра числа:', second_digit)
print('Последняя цифра числа:', last_digit)
