"""
Даны три числа. Найти наименьшее из них.
"""

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

a = 1
b = 3
c = -9

min_digit = min(a, b, c)

logging.info(f'Минимальное число: {min_digit}')
