import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

for i in range(101):
    if i % 3 == 0:
        logging.info(f'Делится на 3: {i}')
