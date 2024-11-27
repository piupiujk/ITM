class ExceptionPrintSendData(Exception):
    def __init__(self, *args):
        # if args:
        #     self.message = args[0]
        # else:
        #     self.message = None

        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка: {self.message}'


raise ExceptionPrintSendData()
