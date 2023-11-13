import time

start = time.time()
iterations = 0
# Check only to the root of the value
found = False
for i in range(999, 99, -1):
    value = int(str(i) + str(i)[::-1])

    for j in range(999, int(value ** 0.5), -1):
        iterations += 1
        other_factor = value // j
        if value % j == 0 and other_factor <= 999 and other_factor >= 100:
            print(value)
            found = True
    
    if found:break

print(f"Elapsed Time: {time.time() - start}")