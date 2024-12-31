# class Dog:
#     __instance = None
#
#     def __init__(self, voice, spices):
#         if Dog.__instance is None:
#             Dog.__instance = self
#             self.voice = voice
#             self.spices = spices
#         else:
#             raise Exception("We can not creat another class")
#
#     @staticmethod
#     def get_instance():
#         # We define the static method to fetch instance
#         if not Dog.__instance:
#             Dog()
#         return Dog.__instance
#
# dog1 = Dog('гав', 'овчарка')
# print(dog1)
#
# dog2 = Dog('гав', 'дворняга').get_instance()
# print(dog2)
#
# dog3 = Dog('гав', 'корги').get_instance()
# print(dog3)
#
# dog4 = Dog('гав', 'шпиц')
# print(dog4)

class Dog:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, voice, spices):
        self.voice = voice
        self.spices = spices

    def make_voice(self):
        print(f'Собака породы {self.spices} сказала {self.voice}')

    def __del__(self):
        Dog.__instance = None

dog1 = Dog('гав', 'овчарка')
print(id(dog1))
dog1.make_voice()

dog2 = Dog('гав', 'корги')
print(id(dog2))
dog2.make_voice()
dog1.make_voice()