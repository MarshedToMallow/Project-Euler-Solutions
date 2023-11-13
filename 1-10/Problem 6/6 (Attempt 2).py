# A polynomial derived in 6.md which computes the difference
def difference(n):
    return ((3 * n + 2) * (n ** 3 - n)) // 12

print(difference(100))