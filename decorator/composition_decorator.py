# ！/usr/bin/python


def get_text(name):
    return "My name is, {0}".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return '<p>{0}</p>'.format(func(name))

    return func_wrapper


my_get_text = p_decorate(get_text)

print(my_get_text("sherlock"))


@p_decorate
def get_text_with_decorator(name):
    return "I'm with decorator {0}".format(name)

print(get_text_with_decorator('lol'))
