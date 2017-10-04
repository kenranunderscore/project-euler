def d(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

divisor_sums = [d(n) for n in range(10001)]

def is_amicable(n):
    d = divisor_sums[n]
    return d <= 10000 and d != n and divisor_sums[d] == n

result = sum([n for n in range(1, 10001) if is_amicable(n)])
print(result)