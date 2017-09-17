def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

digit_factorials = [factorial(n) for n in range(10)]

def is_factorial_sum(n):
    s = sum([digit_factorials[int(x)] for x in str(n)])
    return s == n

result = sum([n for n in range(10, 2540160) if is_factorial_sum(n)])
print(result)