def is_evenly_divisible_by_1_to_20(n):
    for i in range(2, 20):
        if n % i != 0:
            return False
    return True

n = 2520
while not is_evenly_divisible_by_1_to_20(n):
    n += 2520
print(n)
