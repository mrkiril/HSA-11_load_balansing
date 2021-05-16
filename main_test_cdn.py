import asyncio
from functools import wraps

from aiohttp import ClientSession
from aiorun import run
from collections import Counter


def loop_stop(fn):
    @wraps(fn)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_running_loop()
        try:
            return await fn(*args, **kwargs)
        finally:
            loop.stop()
    return wrapper


async def _get_photo(session, url):
    async with session.head(url, allow_redirects=True) as resp:
        # text = await resp.text()
        # print( text )
        return resp.headers.get("X-Node")


@loop_stop
async def main():
    url = "http://projector.localhost:8080/static/cat1.jpg"
    nodes_result = []

    session = ClientSession()
    for i in range(100):
        tasks = [
            asyncio.create_task(_get_photo(session, url))
            for _ in range(100)
        ]
        res = await asyncio.gather(*tasks)
        nodes_result.extend([r for r in res if r is not None])
        print(f"iteration: {i}")

    counter_ = Counter(nodes_result)
    print(f"Riga: {counter_['Riga']}")
    print(f"Berlin: {counter_['Berlin']}")
    print(f"London: {counter_['London']}")

    await session.close()


if __name__ == '__main__':

    print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
    print('= = = = = = = = = = = = = S T A R T   L O A D   P H O T O = = = = = = = = = = = = = = =')
    print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
    run(main(), stop_on_unhandled_errors=True, use_uvloop=True)
    print("BYE ...")
