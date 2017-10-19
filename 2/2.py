import time

start_time = time.clock()

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 1
result = 0
while True:
    fib = fibonacci(n)
    if fib <= 4000000:
        if fib % 2 == 0:
            result += fib
        n += 1
    else:
        break;

duration = time.clock() - start_time

print("The result is {} and was found in {} ms.".format(result, duration))