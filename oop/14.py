from abc import ABC, abstractmethod


class Adder(ABC):
    @abstractmethod
    def add_people(self, people):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass


class SomePeoples(Adder):
    def __init__(self, peoples):
        self.peoples = peoples

    def add_people(self, people):
        self.peoples.append(people)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.peoples) == 0:
            raise StopIteration
        else:
            value = self.peoples[0]
            self.peoples = self.peoples[1:]
            return value


peoples = SomePeoples(['Саша'])

peoples.add_people('Вася')
peoples.add_people('Коля')
peoples.add_people('Дима')

for people in peoples:
    print(people)
