from abc import ABC, abstractmethod


class Animals(ABC):
    @abstractmethod
    def make_voice(self):
        pass


class Cat(Animals):
    def __init__(self, voice):
        self.voice = voice

    def make_voice(self):
        return self.voice


cat1 = Cat('мяу')
print(cat1.make_voice())
