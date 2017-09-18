prev_calcs = dict()

def number_of_distinct_prime_factors(n):
    if n in prev_calcs:
        return prev_calcs[n]
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
    prev_calcs[n] = len(f)
    return len(f)

# here, n is 'foo' iff n and its d - 1 successors have d distinct prime
# factors each
def is_foo(n, d):
    pfls = [number_of_distinct_prime_factors(k) for k in range(n, n + d)]
    return set(pfls) == {d}

def problem47():
    for i in range(210, 200000):
        if is_foo(i, 4):
            return i
    return None

print(problem47())