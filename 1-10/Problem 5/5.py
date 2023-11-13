from timeit import default_timer as timer

start = timer()

smallest = 1

# Iterate over the values 1 to 20
for i in range(1, 21):
    if smallest % i == 0:continue
    smallest_copy = smallest

    # Iterate over the possible factors
    for j in [2] + list(range(3, i + 1)):

        # While it is a factor, divide it from the value
        while i % j == 0:
            i //= j

            # If it isn't a factor of the smallest product, multiply it
            if smallest_copy % j != 0:smallest *= j
            else:smallest_copy //= j
        
        # Break if there are no more factors
        if i == 1:break

print(f"Time Elapsed: {timer() - start}")
print(smallest)