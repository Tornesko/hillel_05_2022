from random import randint
from threading import Thread

lst = []


def fill_list():
    counter = 0
    while counter != 10_000:
        global lst
        lst.append(randint(-100_000, 100_000))
        counter += 1


def get_primes_amount(lst: list) -> int:
    res = 0
    for i in lst:
        res += i
    print(res)
    return res


def get_average():
    sum = 0
    for i in lst:
        sum += i
    res = sum / len(lst)
    print(res)
    return res


t1 = Thread(target=fill_list)

t1.start()
t1.join()
print(len(lst))
t2 = Thread(target=get_primes_amount, kwargs={"lst": lst})
t3 = Thread(target=get_average)

if t1.is_alive() is False:
    t2.start()
    t3.start()
    t2.join()
    t3.join()
