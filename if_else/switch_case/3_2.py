day_month = [31, 10]

match day_month:
    case 28, 2:
        print(1, 3)
    case 31, 1 | 3 | 5 | 7 | 8 | 10:
        print(1, day_month[1] + 1)
    case 30, 4 | 6 | 9 | 11:
        print(1, day_month[1] + 1)
    case 31, 12:
        print(1, 1)
    case _:
        print(day_month[0] + 1, day_month[1])
