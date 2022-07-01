from random import randint
from threading import Thread

lst = []


def fill_list():
    counter = 0
    while counter != 10_000:
        global lst
        lst.append(randint(-1000, 1000))
        counter += 1


def get_primes_amount(lst) -> int:

    return sum(lst)


def get_average(amount: int, n):

    return amount / n


t1 = Thread(target=fill_list)

t1.start()
t1.join()

t2 = Thread(target=get_primes_amount, kwargs={"lst": lst})
t3 = Thread(target=get_average, args=(get_primes_amount(lst), len(lst)))

if t1.is_alive() is False:
    t2.start()
    t3.start()
