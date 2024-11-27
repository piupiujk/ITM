import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

a = int(input())

average = 0
i = 0
while a != 0:
    average += a
    i += 1
    a = int(input())
try:
    logging.info(f'Среднее значение: {average / i}')
except ZeroDivisionError:
    logging.error('Не было введено чисел')