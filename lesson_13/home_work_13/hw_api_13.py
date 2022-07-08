import asyncio
import random
from time import perf_counter

import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 400
SIZE = 1000


def get_random_id() -> str:
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


async def get_pokemon_async() -> str:
    url = BASE_URL + get_random_id()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.json()
            return response.get("name")


def main():
    print("=" * 30)
    start_time = perf_counter()
    tasks = [get_pokemon_async() for _ in range(SIZE)]
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(asyncio.gather(*tasks)))
    loop.close()
    end_time = perf_counter()
    print(f"Execution time: {end_time - start_time}")


if __name__ == "__main__":
    main()
