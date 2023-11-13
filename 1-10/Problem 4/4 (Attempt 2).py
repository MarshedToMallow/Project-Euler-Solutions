from timeit import default_timer as timer

start = timer()
iterations = 0

# Iterate over the possible palindromes
found = False
for i in range(999, 99, -1):
    value = int(str(i) + str(i)[::-1])

    # Check only to the root of the value
    for j in range(999, int(value ** 0.5), -1):
        iterations += 1

        # Check divisibility
        if value % j == 0:

            # Check if the other factor is 3 digits
            other_factor = value // j
            if other_factor <= 999 and other_factor >= 100:
                print(value)
                found = True
                break
    
    if found:break

print(f"Elapsed Time: {timer() - start}")