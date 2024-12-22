class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return self.value + other.value


class Overload(Calculator):
    def add(self, other):
        if isinstance(self.value, (int, float)) and isinstance(other, (int, float)):
            print('Сложили числа')
            return other + self.value
        elif isinstance(self.value, str) and isinstance(other, str):
            print('Сложили строки')
            return other + self.value
        else:
            return 'Разные данные'


calc = Calculator(5)
over = Overload(2)
print(over.add(calc.value))
