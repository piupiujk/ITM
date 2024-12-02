import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

k = 5


s = (1, 2, 3)
match k:
    case 1:
        logging.info('плохо')
    case 2:
        logging.info('неудовлетворительно')
    case 3:
        logging.info('удовлетворительно')
    case 4:
        logging.info('хорошо')
    case 5:
        logging.info('отлично')
    case _:
        logging.critical('Введите число от 1 до 5')

