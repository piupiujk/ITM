import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


def next_date(d, m):
    # Создаём словарь с количеством дней в каждом месяце
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    next_m = m
    # Определяем следующую дату
    if d < days_in_month[m]:
        next_d = d + 1
        if m == 12:
            next_m = 1
    else:
        # Если текущая дата не последняя в месяце, то следующая дата — это первый день следующего месяца
        next_d = 1
        if m == 12:
            next_m = 1
        else:
            next_m = m + 1

    return next_d, next_m


# Пример использования функции
D = int(input("Введите день: "))
M = int(input("Введите месяц: "))
print("Следующая дата:", next_date(D, M))
