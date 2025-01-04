class NewCls:
    def __new__(cls, *args, **kwargs):
        print('Вызов new')
        return super().__new__(cls)

    def __init__(self):
        print('Вызов init')


nc = NewCls()
