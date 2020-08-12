# ！/usr/bin/python

import asyncio
import aiohttp
import json
import itertools


SEARCH_URL = 'https://jobs.github.com/positions.json?'


async def fetch_job_opportunities(session, url):
    async with session.get(url) as response:
        return json.loads(await response.text())


async def main():
    futures = []
    async with aiohttp.ClientSession() as session:
        futures.append(fetch_job_opportunities(session, SEARCH_URL + 'description=Python'))
        futures.append(fetch_job_opportunities(session, SEARCH_URL + 'description=Javascript'))
        futures.append(fetch_job_opportunities(session, SEARCH_URL + 'description=Clojure'))

        results = await asyncio.gather(*futures)
        jobs = list(itertools.chain.from_iterable(results))
        print('Total number of jobs: %s' % len(jobs))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()