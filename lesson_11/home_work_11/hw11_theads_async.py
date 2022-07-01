# EN
#
#     When the application starts, three threads (T1, T2, T3) are launched
#         -T1 thread fills the list with random numbers (10_000 elements)
#         -T2 and T3 threads are waiting when the list is filled
#         -When the list is full T2 and T3 are started
#         -T2 thread finds the sum of the elements of the list
#         -T2 thread finds the arithmetic avarage of the elements of the list
#         -The resulting lists are displayed
#
#     Complete next function

def get_primes_amount(num: int) -> int:
    result = 0
    for i in range(num):
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        result += 1

    return result

numbers = [40000, 400, 1000000, 700]

for i in numbers:
    print(i)

# NOTE: Well, this realization takes too much time...
#       Would be great if I can see less numbers earlier that great numbers :)

# TODO: Complete get_primes_amount function
# TODO: Make this function asyncronous to compute less numbers faster