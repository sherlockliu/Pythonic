# ！/usr/bin/python
from tornado import ioloop, gen


async def cal(num):
    print('cal called.')
    x = await calculator(num)
    print(x)


@gen.coroutine
def calculator(num):
    result = 0
    for i in range(0, num):
        result += i
    print(f'result is {result}')
    return result


async def main():
    await cal(100)
    print('hh')


if __name__ == '__main__':
    # ioloop.IOLoop.current().start()
    # main()
    ioloop.IOLoop.current().run_sync(main)

