import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

month = 2

month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [2, 4, 6, 9, 11]

match month:
    case 2:
        print('28 дней')
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print('31 день')
    case 2 | 4 | 6 | 9 | 11:
        print('30 дней')
