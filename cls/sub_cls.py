# ！/usr/bin/python


class BaseClass:
    def __init__(self):
        self.key = "hhh"

    def test(self):
        print('This is base class')


class SubClassA(BaseClass):
    pass


class SubClassB(BaseClass):
    def test(self):
        super(SubClassB, self).test()
        print('this is subclass b')

    def get_key(self):
        print(self.key)

print(isinstance(SubClassA(), BaseClass))

#
# sa = SubClassA()
# sa.test()
#
# sb = SubClassB()
# sb.test()
#

# class Base:
#     def __init__(self):
#         print('Base called.')
#
#     def test(self):
#         print('Base test called.')
#
#
# class BaseA(Base):
#     def __init__(self):
#         print('BassA called.')
#         super(BaseA, self).__init__()
#
#     def test(self):
#         print('BaseA test called.')
#
#
# class BaseB(Base):
#     def __init__(self):
#         print('BaseB called.')
#         # super(BaseB, self).__init__()
#
#     def test(self):
#         print('BaseB test called.')
#
#
# class SubA(BaseA, BaseB):
#     def __init__(self):
#         print('Sub class called.')
#         BaseA.__init__(self)
#         # BaseB.__init__(self)
#
#
# # a = SubA()
# a = BaseA()
# a.test()
# a.test()
# SubClassB().get_key()
# left --> right --> top
