value = 600851475143
potential_factor = 3

# Continue until value equals than the potential_factor
while value != potential_factor:

    # If a factor is found, it is divided out
    if value % potential_factor == 0:value //= potential_factor

    # Otherwise the potential_factor increases by 2 (Only enabled when no factor is found, just in case there's a duplicate factor)
    else:potential_factor += 2

# The final result
print(potential_factor)