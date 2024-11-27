import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

for i in range(1, 21):
    logging.info(f'{i/2} ** 2 = {(i/2)**2}')