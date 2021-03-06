import time

import tornado.web
from tornado.gen import multi


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        await multi([self.fn_a(), self.fn_b()])
        # await self.fn_a()
        # await self.fn_b()

    async def fn_a(secs):
        print(f'A Start : {time.ctime()}')
        time.sleep(5)
        print(f'A End : {time.ctime()}')

    async def fn_b(secs):
        print(f'B Start : {time.ctime()}')
        time.sleep(5)
        print(f'B End : {time.ctime()}')


class SleepHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(5)
        self.write('finish')


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/sleep", SleepHandler),
    ])
    application.listen(18888)
    tornado.ioloop.IOLoop.current().start()
