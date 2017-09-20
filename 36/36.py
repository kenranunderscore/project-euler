def is_doubly_palindromic(n):
    d = str(n)
    b = "{0:b}".format(n)
    return d == d[::-1] and b == b[::-1]

palindromes = [n for n in range(1, 1000000) if is_doubly_palindromic(n)]
print(sum(palindromes))