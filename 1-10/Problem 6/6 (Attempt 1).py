# The closed form of the sum from 1 to n
def squared_sum(n):
    sum_ = (n * (n + 1)) // 2
    return sum_ * sum_

# A polynomial derived in 6.md which computes the sum of the squares
def summed_squares(n):
    a = (n * n * n) / 3
    b = (n * n) / 2
    c = n / 6
    return int(a + b + c)

print(squared_sum(100) - summed_squares(100))