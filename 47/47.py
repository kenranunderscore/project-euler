def number_of_distinct_prime_factors(n):
    f = set()
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            f.add(i)
    if n > 1:
        f.add(n)
    return len(f)

# here, n is 'foo' iff n and its d - 1 successors have d distinct prime
# factors each
def is_foo(n, d):
    pfls = [number_of_distinct_prime_factors(k) for k in range(n, n + d)]
    return set(pfls) == {d}

def problem47():
    for i in range(10, 200000):
        if is_foo(i, 4):
            return i
    return None

print(problem47())