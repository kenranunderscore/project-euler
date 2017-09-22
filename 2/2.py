def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 1
sum = 0
while True:
    fib = fibonacci(n)
    if fib <= 4000000:
        if fib % 2 == 0:
            sum += fib
        n += 1
    else:
        break;
print(sum)