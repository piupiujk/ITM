"""
Даны два числа. Вывести большее из них.
"""

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

a = 3
b = 3

if a > b:
    logging.info(f'Наибольше число: {a}')
elif b > a:
    logging.info(f'Наибольше число: {b}')
else:
    logging.info(f'Числа равны')