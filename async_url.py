import asyncio
import aiohttp

#global list of correct urls, there's probably better way to do this
correct = []

#check the url with a 5 seconds timeout and if the url has a 200 status code it will raise an exception and append to the correct url's list
async def check(url, session):
    session : aiohttp.ClientSession
    async with session.get(url, timeout=5) as response:
        if response.status == 200:
            correct.append(url)
            raise Exception

#create the tasks and run, if an exception is raised, stop the execution and cancel the remaining ones
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

#return the last result from the correct url's list
def get_correct_url(urls):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(multiprocessing_func(urls))
    return(correct[-1])
