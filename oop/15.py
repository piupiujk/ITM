import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class Any:
    def __init__(self, any, some, something):
        self.any = any
        self.some = some
        self.something = something

    def __setattr__(self, key, value):
        if key in self.__dict__:
            old_value = self.__dict__[key]
        else:
            old_value = value
        self.__dict__[key] = value
        logging.info(f'Атрибут {key} был изменен {old_value} -> {self.__dict__[key]}')


anys = Any(1, 2, 3)
anys.any = 3
anys.any = 5
anys.some = 1
