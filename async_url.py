import asyncio
import aiohttp

correct = []

async def check(url, session):
    session : aiohttp.ClientSession
    async with session.get(url, timeout=5) as response:
        if response.status == 200:
            correct.append(url)
            raise Exception

async def multiprocessing_func(url_list):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in url_list:
            tasks.append(asyncio.create_task(check(i, session)))
        try:
            return await asyncio.gather(*tasks)
        except:
            for t in tasks:
                t.cancel()


def getUrl(urls):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(multiprocessing_func(urls))
    return(correct[-1])
