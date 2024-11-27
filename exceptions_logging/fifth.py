import logging
import math

logging.basicConfig(level=logging.INFO, filename="py_log_5.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


def solving_quadratic():
    while True:
        print("Введите коэффициенты для уравнения")
        print("ax^2 + bx + c = 0:")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        discr = b ** 2 - 4 * a * c

        if discr > 0:
            try:
                1 / a
            except ZeroDivisionError as e:
                print('Деление на ноль!')
                logging.error('ZeroDivisionError', exc_info=e)
            else:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                print(f"x1 = {x1}\nx2 = {x2}")
                logging.info('The roots have been found: x1 - %s, x2 - %s', x1, x2)
                break
        elif discr == 0:
            try:
                1 / a
            except ZeroDivisionError as e:
                print('Деление на ноль!')
                logging.error('ZeroDivisionError', exc_info=e)
            else:
                x = -b / (2 * a)
                print(f"x = {x}")
                logging.info(f'The root is found: x - %s', x)
                break
        else:
            print('Дискриминант меньше нуля')
            logging.error('The discriminant is less than zero')


solving_quadratic()
