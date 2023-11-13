count_3, count_5 = 3, 5
total = 0

# Continue until both values are at least 1000
while count_3 < 1000 or count_5 < 1000:

    # Add the smaller value to the total
    total += min(count_3, count_5)

    # Increase the smaller value by its corresponding amount (or both if equivalent)
    if count_3 < count_5:count_3 += 3
    elif count_3 > count_5:count_5 += 5
    else:
        count_3 += 3
        count_5 += 5

# The final result
print(total)