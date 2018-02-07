# ！/usr/bin/python


def html_tag(tag_name):
    def tag_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name,func(name))
        return  func_wrapper
    return  tag_decorator


@html_tag('div')
@html_tag('strong')
@html_tag('p')
def get_text(name):
    return "hello " + name


print(get_text('sherlock'))

