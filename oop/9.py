class Car:
    def __call__(self, *args, **kwargs):
        print('Вызов экземпляра как функцию')

    def __new__(cls, *args, **kwargs):
        print('Вызван метод __new__')
        return super().__new__(cls)

    def __init__(self, color, weight, *args):
        self.color = color
        self.coords = list(args)
        self.weight = weight

    def __repr__(self):
        return f'{self.__class__}: {self.color}'

    def __len__(self):
        return len(self.color)

    def __abs__(self):
        return list(map(abs, self.coords))

    def __add__(self, other):
        return Car(self.color, self.weight + other, *self.coords)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.weight += other
        return self

    def __eq__(self, other):
        return self.weight == other

    def __ne__(self, other):
        return self.weight != other

    def __le__(self, other):
        return self.weight <= other

    def __ge__(self, other):
        return self.weight >= other

    def __gt__(self, other):
        return self.weight > other

    def __lt__(self, other):
        return self.weight < other

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.coords) == 0:
            raise StopIteration
        else:
            value = self.coords[0]
            self.coords = self.coords[1:]
            return value

    def __getitem__(self, item):
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value

    def __delitem__(self, key):
        del self.coords[key]

    def __del__(self):
        print('Данные удалены')

    def __str__(self):
        return 'Экземпляр класса Car'

    def __getattr__(self, item):
        return 'Данного атрибута не существует'

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(f'Присвоение атрибуту {key} значение {value}')

    def __getattribute__(self, item):
        print("Вызван метод __getattribute__")
        return super().__getattribute__(item)

    def __bool__(self):
        return self.coords[0] == self.coords[1]

    def __hash__(self):
        return hash(self.coords)


car = Car('black', 900, 800, 1200)
car2 = Car('red', 500, 800, 700)

