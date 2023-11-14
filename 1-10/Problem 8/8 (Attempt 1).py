import math, timeit

start = timeit.default_timer()

with open("8 (Number).txt") as f:
    number = f.read()

# Exclude the starting indices which have a zero from the pool of potential candidates
index = 999
candidates = set(range(1000))
while index >= 0:
    digit = number[index]
    if digit == "0":

        # Keep removing candidates until there aren't any zeros
        offset = 0
        while offset < 13:
            candidates.discard(index - offset)
            offset += 1
            if number[index - offset] == "0":
                index -= offset
                offset = 0
        
        # Skip the affected indices
        index -= 13

    else:index -= 1

# Iterate over the candidates, saving the largest product
best = 0
for index in candidates:
    digits = [int(i) for i in number[index:index + 13]]
    product = math.prod(digits)
    best = max(best, product)

print(timeit.default_timer() - start)
print(best)