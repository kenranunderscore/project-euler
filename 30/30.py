def is_5th_power_sum(n):
    s = sum([int(x) ** 5 for x in str(n)])
    return s == n

numbers = [n for n in range(10, 300001) if is_5th_power_sum(n)]
print(sum(numbers))