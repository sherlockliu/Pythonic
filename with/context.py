# ！/usr/bin/python


class Context:
    def __enter__(self):
        print('Enter the zone.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('leaving the zone.')
        if exc_type is None:
            print('with no error.')
        else:
            print(f'with an error {exc_val}')


with Context():
    print('I am the zone.')

with Context():
    print('I am the buggy zone.')
    raise TypeError('I am the bug.')
