import math


class Figure:
    def get_pr(self):
        return -1
        # raise ValueError('В каждом классе должен быть переопределен метод get_pr()')


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_pr(self):
        return (self.a + self.b) * 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


class Circle(Figure):
    def __init__(self, r):
        self.r = r
    #
    # def get_pr(self):
    #     return 2 * math.pi * self.r


figures = [Rectangle(2, 5), Rectangle(1, 9),
           Triangle(1, 2, 3), Triangle(4, 6, 3),
           Circle(5), Circle(8)]

for figure in figures:
    print(figure.get_pr())
