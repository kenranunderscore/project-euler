def fibonacci(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a + b, a
        n -= 1
    return a

n = 1
while len(str(fibonacci(n))) < 1000:
    print(n)
    n += 1
print(n)