value = 600851475143
largest_factor = None
factor = 3

# Continue until all factors are divided out
while value != 1:

    # If a factor is found, then it is saved as the largest factor
    if value % factor == 0:
        value //= factor
        largest_factor = factor

    # Otherwise the factor increases by 2
    else:factor += 2

# The final result
print(largest_factor)