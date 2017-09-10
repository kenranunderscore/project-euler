def findLargestPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

print(findLargestPrimeFactor(600851475143))
