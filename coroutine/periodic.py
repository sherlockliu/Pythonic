# ！/usr/bin/python
import asyncio
import aiohttp
import time

running = True


async def check_status_periodically():
    async with aiohttp.ClientSession() as session:
        while running:
            async with session.head('https://www.google.com') as response:
                print(response.status, time.strftime("%H:%M:%S", time.localtime(time.time())))
            await asyncio.sleep(2)

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(check_status_periodically())
        loop.run_forever()
    except KeyboardInterrupt:
        running = False
    finally:
        pending = asyncio.Task.all_tasks()
        loop.run_until_complete(asyncio.gather(*pending))
        loop.close()
        print('\nDone')
