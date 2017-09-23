numbers = [str(n) for n in range(1, 200000)]
s = "".join(numbers)

def d(n):
    return int(s[n - 1])

result = d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
print(result)