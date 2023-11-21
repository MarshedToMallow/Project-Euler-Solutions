import timeit

primes = [2]
counts = [2]
current = 2
previous = None

THRESHOLD = 20000

start = timeit.default_timer()

while True:
    previous = current

    index = min(range(len(primes)), key = lambda x: primes[x] + counts[x])

    counts[index] += primes[index]
    current = counts[index]

    if current == previous:continue
    
    if current - previous > 1:
        primes.append(current - 1)
        counts.append(current - 1)
        #if len(primes) % 1000 == 0:print("m")
        #if len(primes) % 10000 == 0:print(f"{len(primes)} @ {timeit.default_timer() - start}")

    if primes[-1] > THRESHOLD:
        del primes[-1]
        break

print(f"Time: {timeit.default_timer() - start}")

print(f"Sum of primes: {sum(primes):,}")
print(f"Primes under {THRESHOLD:,}: {len(primes):,}")