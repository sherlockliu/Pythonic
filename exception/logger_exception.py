# ！/usr/bin/python
import logging


def log_exception():
    try:
        raise Exception('kk')
    except Exception as e:
        logging.error(e)
    return 'lll'


l = log_exception()

print(l)
