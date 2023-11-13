import time

start = time.time()

# Start with the squares of valid values
products = [i ** 2 for i in range(100, 1000)]

while True:

    # Get the largest value
    value = max(products)

    # Check if value is a palindrome
    if str(value) == str(value)[::-1]:
        print(value)
        break
    
    # If not, decrement it by the index + 100
    index = products.index(value)
    products[index] -= (index + 100)

print(f"Elapsed time: {time.time() - start}")