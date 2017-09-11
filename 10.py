def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
 
sum = 0
n = 2
while n < 2000000:
    if is_prime(n):
        sum += n
    n += 1
print(sum)
