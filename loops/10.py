import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        logging.info(f'Простое число: {num}')
