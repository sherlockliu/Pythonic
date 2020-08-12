# ！/usr/bin/python


def my_generator():
    try:
        yield 'OK'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print("OK,let's clean.")


gen = my_generator()
gen.__next__()
gen.throw(ValueError('mean mean mean'))
gen.close()
