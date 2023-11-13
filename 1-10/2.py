x, y = 2, 8
total = 0

# Continue until x is at least 4,000,000
while x <= 4000000:
    
    # Add x to the total
    total += x

    # Set x to y and set y to the fibonacci value 3 places ahead
    x, y = y, x + 4 * y

# The final result
print(total)