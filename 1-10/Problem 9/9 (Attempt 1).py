import timeit

start = timeit.default_timer()

goal = 1000
found = False

# c can start from goal // 3 + 1 since it needs to be larger than the other two
for c in range(goal // 3 + 1, goal - 1):
    a_plus_b = goal - c
    c_squared = c * c

    # b can start from a_plus_b // 2 since it needs to be larger than a
    for b in range(a_plus_b // 2, a_plus_b):

        # Calculating a from (essentially) goal - (b + c) rather than iterating over it or using the other formula ((c^2 - b^2)^0.5)
        a = a_plus_b - b
        if a == b:continue

        a_squared_sum_b = a * a + b * b

        # Break if success
        if a_squared_sum_b == c_squared:
            found = True
            break

        # If a^2 + b^2 is already larger than c^2, it won't go down until c gets larger, so we break back to the outer loop
        elif a_squared_sum_b > c_squared:break
    
    if found:break

print("Time Elapsed:", timeit.default_timer() - start)
print(f"{a} + {b} + {c} = 1,000 and {a}^2 + {b}^2 = {c}^2 ({a**2:,} + {b**2:,} = {c**2:,})")