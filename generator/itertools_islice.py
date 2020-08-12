# ！/usr/bin/python

import itertools


def starting_at_five():
    value = input().strip()
    while value != '':
        for el in itertools.islice(value.split(), 4, None):
            yield el
        value = input().strip()


my_iter = starting_at_five()
