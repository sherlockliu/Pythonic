# ！/usr/bin/python

from itertools import groupby


def compress(data):
    return ((len(list(group)), name) for name, group in groupby(data))


def decompress(data):
    return (car * size for size, car in data)


my_data = 'get uuuuuuuuuuuuuuuup'
print(list(my_data))

compressed = compress(my_data)
print(''.join(decompress(compressed)))
