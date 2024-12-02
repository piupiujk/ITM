"""
Даны три целых числа. Найти количество положительных чисел в исходном наборе.
"""
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

a = 1
b = 3
c = -9

count = 0

if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1

logging.info(f'Количество положительных чисел: {count}')