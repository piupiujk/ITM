import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

digits = [1, 2, 3, 4, 6, 2, 6]

for digit in digits:
    logging.info(f'Текущее число: {digit}')

ages = {
    'Alex': 25,
    'Jhon': 18,
    'Bred': 33,
    'Lion': 40
}

for name in ages:
    logging.info(f'Name - {name}, age - {ages[name]}')
