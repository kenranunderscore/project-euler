import time

start_time = time.clock()

def fibonacci(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a + b, a
        n -= 1
    return a

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