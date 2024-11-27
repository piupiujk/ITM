import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

for i in range(1, 11):
    logging.info(f'2 * {i} = {2 * i}')
