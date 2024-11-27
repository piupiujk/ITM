import logging
from random import randint


def randomizer():
    numbers = []

    while True:
        print('Введите колличество случайных чисел count и их диапозон от a до b')
        count = input('count = ')
        try:
            count = int(count)
        except ValueError:
            print('Количество должно быть целым числом!')
            logging.error('The quantity is not an integer')
        else:
            if count > 0:
                a = input('a = ')
                b = input('b = ')
                try:
                    a = int(a)
                    b = int(b)
                except ValueError:
                    print('a и b должны быть числами')
                    logging.error('a and b is not numbers')
                else:
                    if a < b:
                        for i in range(count):
                            number = randint(a, b)
                            numbers.append(number)
                        print(f'Случайные числа: {numbers}')
                        logging.info('Random numbers: %s', numbers)
                        break
                    else:
                        print('a должно быть больше b')
                        logging.error('a is less than b')
            else:
                print('Количество не может быть меньше или равно нулю!')
                logging.error('Quantity is a negative number')


logging.basicConfig(level=logging.INFO, filename="py_log_6.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

randomizer()
