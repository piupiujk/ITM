import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

"""
N - север
W - запад
S - юг
E - восток
"""

cmd = ('E', 0)
match cmd:
    case 'N', 0:
        print('Смотрит на север')
    case 'N', 1:
        print('Смотрит на запад')
    case 'N', -1:
        print('Смотрит на юг')
    case 'W', 0:
        print('Смотрит на запад')
    case 'W', 1:
        print('Смотрит на юг')
    case 'W', -1:
        print('Смотрит на север')
    case 'S', 0:
        print('Смотрит на юг')
    case 'S', 1:
        print('Смотрит на восток')
    case 'S', -1:
        print('Смотрит на запад')
    case 'E', 0:
        print('Смотрит на восток')
    case 'E', 1:
        print('Смотрит на север')
    case 'E', -1:
        print('Смотрит на юг')
    case _: print('Неизвестная команда')
