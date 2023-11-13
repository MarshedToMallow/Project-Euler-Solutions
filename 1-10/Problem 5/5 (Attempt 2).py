from timeit import default_timer as timer

start = timer()

# Increase each iteration by the product of the primes 1 to 20
increase = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
value = 0
found = False

while not found:
    found = True
    value += increase

    # Check divisibility by each number 1 to 20
    for i in range(1, 21):
        if value % i != 0:
            found = False
            break

print("Time Elapsed:", timer() - start)
print(value)