import timeit

start_time = timeit.default_timer()

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

duration = timeit.default_timer() - start_time

lpf = largest_prime_factor(600851475143)
msg = "The largest prime factor of {0} is {1} and was found in {2:.9f} seconds."
print(msg.format(600851475143, lpf, duration))