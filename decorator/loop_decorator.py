# ！/usr/bin/python


def p_decorator(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper


def strong_decorator(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))

    return func_wrapper


def div_decorator(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))

    return func_wrapper


def get_text(name):
    return 'Hello ' + name

func = div_decorator(strong_decorator(p_decorator(get_text)))

print(func('sherlock'))


@div_decorator
@strong_decorator
@p_decorator
def get_greet(name):
    return get_text(name)

print(get_greet('Sherlock'))
