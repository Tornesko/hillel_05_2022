import asyncio


async def get_primes_amount(num: int) -> int:
    lst = [1]
    k = 0
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                k += 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
        await asyncio.sleep(0)
    print(len(lst))

    return len(lst)


numbers = [100, 40000, 400, 1000000, 700, 3500, 65000, 20, 12000, 73]

tasks = [
    get_primes_amount(
        i,
    )
    for i in numbers
]

main_loop = asyncio.get_event_loop()

main_loop.run_until_complete(asyncio.gather(*tasks))
main_loop.close()


# Я СДЕЛЯЛЬ :D
# output:
# _________________________________
# 9
# 22
# 26
# 79
# 126
# 490
# 1439
# 4204
# 6494
# _________________________________
# я не став чекати доки воно мільйон вирахує


# TODO: Make this function asynchronous to compute less numbers faster
