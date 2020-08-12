# ！/usr/bin/python


my_iter = (x ** 2 for x in range(10) if x % 2 == 0)
for el in my_iter:
    print(el)

my_list = [x ** 2 for x in range(10) if x % 2 == 0]
for i, el in enumerate(my_list):
    print(f'{i} is {el}')
