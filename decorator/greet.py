# ！/usr/bin/python


def greet(name):
    return 'hello ' + name


greet_someone = greet
print(greet_someone('sherlock'))


def greet_outside(name):
    def get_message():
        return 'Hello '

    result = get_message() + name
    return result


print(greet_outside('Sherlock'))


def call_func(func):
    other_name = "Winston"
    return func(other_name)


print(call_func(greet))


def compose_greet_func(name):
    def get_message():
        return 'Hello there!' + name

    return get_message

c_greet = compose_greet_func('Mr liu')
print(c_greet())

