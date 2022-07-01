def get_primes_amount(num: int) -> int:
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

    return len(lst)


numbers = [40000, 400, 1000000, 700]

for i in numbers:
    print(get_primes_amount(i))

# NOTE: Well, this realization takes too much time...
#       Would be great if I can see less numbers earlier that great numbers :)


# TODO: Make this function asyncronous to compute less numbers faster
