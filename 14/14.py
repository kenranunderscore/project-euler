def collatz(n):
    s = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        s.append(n)
    return s + [1]

max = 0
n = 1
for i in range(1, 1000000):
    length = len(collatz(i))
    if length > max:
        n = i
        max = length
print(n)
print(length)