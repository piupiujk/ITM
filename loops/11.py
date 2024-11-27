import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

count = 0
for i in range(1, 11):
    count += i**2

logging.info(f'Сумма квадратов: {count}')
