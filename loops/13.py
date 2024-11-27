import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

for i in range(1, 6):
    fact = 1
    for j in range(1, i+1):
        fact *= j

    logging.info(f'Факториал {i} = {fact}')
