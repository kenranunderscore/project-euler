digit_powers = [x ** 5 for x in range(10)]

def is_5th_power_sum(n):
    s = sum([digit_powers[int(x)] for x in str(n)])
    return s == n

result = sum([n for n in range(10, 300001) if is_5th_power_sum(n)])
print(result)