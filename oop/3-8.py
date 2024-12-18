class MeansOfTransport:
    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

    def show_color(self):
        print(f'Цвет транспортного средства: {self.__color}')

    def show_brand(self):
        print(f'Марка транспортного средства: {self.__brand}')

    # 4 задание - сеттеры, геттеры
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def set_color(self, new_color):
        self.__color = new_color

    def get_brand(self):
        return self.__brand

    def get_color(self):
        return self.__color


# 5 задание
class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, brand, color, amount_wheel):
        super().__init__(brand, color)
        self.__amount_wheel = amount_wheel

    # 8 задание
    @classmethod
    def get_drivers(cls):
        return cls.car_drive

    def __del__(self):
        print('Данные удалены')

    def __str__(self):
        return 'Экземпляр класса Car'

    def __getattr__(self, item):
        return 'Данного атрибута не существует'

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(f'Присвоение атрибуту {key} значение {value}')


car1 = Car('audi', 'black', 3)
print(car1.get_drivers())
print(car1)
print(car1.name)


class Moped(MeansOfTransport):
    def __init__(self, brand, color, amount_wheel):
        super().__init__(brand, color)
        self.__amount_wheel = amount_wheel

    # 6 задание
    @staticmethod
    def get_time(distance, max_speed):
        return f'Время: {(distance / max_speed) * 60} минут'

# moped1 = Moped('audi', 'black', 3)
# print(moped1.get_time(10, 100))
