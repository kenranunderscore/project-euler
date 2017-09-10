def isPalindrome(n):
    s = str(n)
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def palindromes():
    result = []
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j
            if isPalindrome(product):
                result.append(product)
    return result

print(max(palindromes()))
