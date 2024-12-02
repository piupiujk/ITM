"""
Даны координаты точки, не лежащей на координатных осях OX и OY.
Определить номер координатной четверти, в которой находится данная точка.
Координаты задаются пользователем, например (10, 15).
"""

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

x = 10
y = 15

if x > 0:
    if y > 0:
        logging.info(f'Точка находится в 1 четверти')
    else:
        logging.info(f'Точка находится в 4 четверти')
else:
    if y > 0:
        logging.info(f'Точка находится в 2 четверти')
    else:
        logging.info(f'Точка находится в 3 четверти')
