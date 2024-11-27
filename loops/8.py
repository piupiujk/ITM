import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

count = 0
for i in range(1, 101):
    count += i
logging.info(f'Сумма всех чисел: {count}')