def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

primes = []
n = 2
while len(primes) <= 10001:
    if is_prime(n):
        primes.append(n)
    n += 1

print(primes[10000])
