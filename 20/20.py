def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(sum([int(x) for x in str(factorial(100))]))