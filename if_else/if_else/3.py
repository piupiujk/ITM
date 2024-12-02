"""
Даны два числа. Вывести вначале большее, а затем меньшее из них.
"""

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

a = 3
b = 4

if a > b:
    logging.info(f'{a} {b}')
elif b > a:
    logging.info(f'{b} {a}')
else:
    logging.info(f'Числа равны')
