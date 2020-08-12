# ！/usr/bin/python
import sys
import traceback


def test():
    try:
        a = 10 / 10
    except ZeroDivisionError as p:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        trace = traceback.format_exception(
            exc_type, exc_value, exc_traceback
        )
        print(trace)
    except Exception as e:
        print("hello, world")
        print(repr(e))
    try:
        print(a)
    except:
        pass

def wrapper_error():
    try:
        raise KeyError('hhh')
    except Exception as e:
        raise e

def run():
    try:
        wrapper_error()
    except KeyError as ke:
        print('OK')
        print(ke)


# def redact():
#     try:
#         json.loads('{"a":1,"b"')
#     except Exception as e:
#         print(repr(e))
# redact()
run()