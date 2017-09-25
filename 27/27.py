import time

start_time = time.time()

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def consecutive_primes(a, b):
    n = 0
    while is_prime(n * n + a * n + b):
        n += 1
    return n

max_a, max_b, max_n = 0, 0, 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = consecutive_primes(a, b)
        if n > max_n:
            max_a, max_b, max_n = a, b, n
print(max_a)
print(max_b)
print(max_n)
print(max_a * max_b)

print("Duration: {} ms".format(time.time() - start_time))