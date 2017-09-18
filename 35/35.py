def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def is_circular_prime(n):
    for m in rotations(n):
        if not is_prime(m):
            return False
    return True

count = 0
for n in range(2, 1000000):
    if is_circular_prime(n):
        count += 1
print(count)