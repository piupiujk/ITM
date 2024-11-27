import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

for i in range(0, 101):
    logging.info(f'Number: {i}')