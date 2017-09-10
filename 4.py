def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

def palindromes():
    result = []
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j
            if isPalindrome(product):
                result.append(product)
    return result

print(max(palindromes()))
