def divisor_count(n):
    count = 0
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            count += 1
    return count

def nth_triangle_no_divisor_count(n):
    if n % 2 == 0:
        return divisor_count(int(n/2)) * divisor_count(n + 1)
    else:
        return divisor_count(n) * divisor_count(int((n + 1)/2))

for n in range(1, 1000000):
    if nth_triangle_no_divisor_count(n) >= 500:
        print(int(n * (n + 1) / 2))
        break
