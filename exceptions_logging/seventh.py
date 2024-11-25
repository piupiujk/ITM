import logging


def find_average(numbers: list):
    average = 0
    for num in numbers:
        average += num
    return average / len(numbers)


logging.basicConfig(level=logging.INFO, filename="py_log_7.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

numbers = [1, 2, '']
try:
    print(find_average(numbers))
except:
    print('Введите список чисел')
    logging.error('A list of non-numbers has been entered')
