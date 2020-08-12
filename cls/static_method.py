# ！/usr/bin/python

class Monday:
    def __init__(self,name):
        name = name
    xx = '1'
    @staticmethod
    def print_word(w):
        print(w)

    @classmethod
    def class_method(cls,x):
        print(x)

    def fn(self, y):
        print(y)

Monday().print_word('hhh')
Monday.print_word('hhhxxx')
Monday.fn('x')

