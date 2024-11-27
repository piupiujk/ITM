import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

for i in range(10):
    logging.info(f'Проход по числу {i}')
    for j in range(10):
        logging.info(f'{i} * {j} = {i * j}')
