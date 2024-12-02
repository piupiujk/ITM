num = 917
digits_num = [num // 100, (num % 100) // 10, num % 10]
print(digits_num)
num_word = ''

match digits_num:
    case [1, _, _]:
        num_word += 'сто '
    case [2, _, _]:
        num_word += 'двести '
    case [3, _, _]:
        num_word += 'триста '
    case [4, _, _]:
        num_word += 'четыриста '
    case [5, _, _]:
        num_word += 'пятьсот '
    case [6, _, _]:
        num_word += 'шестьсот '
    case [7, _, _]:
        num_word += 'семьсот '
    case [8, _, _]:
        num_word += 'восемьсот '
    case [9, _, _]:
        num_word += 'девятьсот '

match digits_num:
    case [_, 1, 0]:
        num_word += 'десять '
    case [_, 1, 1]:
        num_word += 'одиннадцать '
    case [_, 1, 2]:
        num_word += 'двенадцать '
    case [_, 1, 3]:
        num_word += 'тринадцать '
    case [_, 1, 4]:
        num_word += 'четырнадцать '
    case [_, 1, 5]:
        num_word += 'пятнадцать '
    case [_, 1, 6]:
        num_word += 'шестнадцать '
    case [_, 1, 7]:
        num_word += 'семнадцать '
    case [_, 1, 8]:
        num_word += 'восемнадцать '
    case [_, 1, 9]:
        num_word += 'девятнадцать '
    case [_, 2, _]:
        num_word += 'двадцать '
    case [_, 3, _]:
        num_word += 'тридцать '
    case [_, 4, _]:
        num_word += 'сорок '
    case [_, 5, _]:
        num_word += 'пятьдесят '
    case [_, 6, _]:
        num_word += 'шестьдесят '
    case [_, 7, _]:
        num_word += 'семьдесят '
    case [_, 8, _]:
        num_word += 'восемьдесят '
    case [_, 9, _]:
        num_word += 'девяносто '

match digits_num:
    case [_, 1, _]:
        pass
    case [_, _, 1]:
        num_word += 'один'
    case [_, _, 2]:
        num_word += 'два'
    case [_, _, 3]:
        num_word += 'три'
    case [_, _, 4]:
        num_word += 'четыре'
    case [_, _, 5]:
        num_word += 'пять'
    case [_, _, 6]:
        num_word += 'шесть'
    case [_, _, 7]:
        num_word += 'семь'
    case [_, _, 8]:
        num_word += 'восемь'
    case [_, _, 9]:
        num_word += 'девять'

print(num_word)

