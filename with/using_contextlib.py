# ！/usr/bin/python

from __future__ import with_statement
from contextlib import contextmanager


@contextmanager
def context():
    print('entering the zone.')
    try:
        yield
    except Exception as e:
        print(f'With an error {e}')
        raise e
    else:
        print('with no error')


with context():
    print('I am the zone.')

with context():
    print('I am the buggy zone.')
    raise TypeError('I am the bug.')
