def divisor_sum(n):
    return sum([i for i in range(1, n // 2 + 1) if n % i == 0])

def is_abundant(n):
    return divisor_sum(n) > n

abundant_numbers = [n for n in range(1, 28123) if is_abundant(n)]
sums = set()
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        s = abundant_numbers[i] + abundant_numbers[j]
        sums.add(s)

result = sum([n for n in range(1, 28124) if n not in sums])
print(result)