# ！/usr/bin/python
import asyncio
import time


async def wait_for_stuff():
    start = time.time()
    for i in range(0, 5):
        await asyncio.sleep(2)
    print('Time elapsed: %d seconds' % int(time.time() - start))


async def wait_for_stuff_con():
    start = time.time()
    futures = []
    for i in range(0, 5):
        futures.append(asyncio.sleep(1))

    await asyncio.wait(futures)

    print('Time elapsed: %d seconds' % int(time.time() - start))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(wait_for_stuff_con())
    finally:
        loop.close()
