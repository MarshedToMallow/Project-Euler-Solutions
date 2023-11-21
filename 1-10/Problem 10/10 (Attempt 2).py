import timeit

primes = [2000000]

HELPER_COUNT = 45
helpers = [2]
candidate = 3

while len(helpers) != HELPER_COUNT:
    is_prime = True
    for prime in helpers:
        if candidate % prime == 0:
            is_prime = False
            break
    if is_prime:helpers.append(candidate)
    candidate += 2

start = timeit.default_timer()

for candidate in range(primes[0] - 1, 1, -1):

    remove = []

    for index, prime in enumerate(primes):
        if prime % candidate == 0:
            remove.append(index)
        if candidate * candidate > prime:break

    for index in sorted(remove, reverse = True):
        del primes[index]

    if not any([(candidate % i == 0) and (candidate != i) for i in helpers]):primes.append(candidate)

print(timeit.default_timer() - start)

#print(primes[::-1])
print(len(primes))
print(sum(primes))