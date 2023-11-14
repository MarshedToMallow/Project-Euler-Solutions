prime_count = 1
number = 1

# Iterate until the 10,001st prime
while prime_count < 10001:
    number += 2
    is_prime = True

    # If any factors evenly divide the number, it isn't prime
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            is_prime = False
            break
    
    if is_prime:prime_count += 1
print(number)