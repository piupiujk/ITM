class Transport:
    def __init__(self, brand, country, color):
        self.__brand = brand
        self.__country = country
        self.color = color

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def get_brand(self):
        return self.__brand

car = Transport('BMW', 'Germany', 'black')
print(car.get_brand())
car.set_brand('Mercedes')
print(car.get_brand())
print(car.__dict__)
