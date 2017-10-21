import timeit

start_time = timeit.default_timer()

def is_palindrome(n):
    s = str(n)
    s_reversed = s[::-1]
    return s == s_reversed

def palindromes():
    result = []
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j
            if is_palindrome(product):
                result.append(product)
    return result

largest_palindrome = max(palindromes())
duration = timeit.default_timer() - start_time
msg = "Largest palindrome {0} found in {1:.5f} seconds."
print(msg.format(largest_palindrome, duration))