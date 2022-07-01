#     When the application starts, three threads (T1, T2, T3) are launched
#         -T1 thread fills the list with random numbers (10_000 elements)
#         -T2 and T3 threads are waiting when the list is filled
#         -When the list is full T2 and T3 are started
#         -T2 thread finds the sum of the elements of the list
#         -T2 thread finds the arithmetic average of the elements of the list
#         -The resulting lists are displayed

from random import randint
from threading import *

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
