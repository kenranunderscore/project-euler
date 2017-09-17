def sum_of_squares(n):
    return n * (n+1) * (2*n+1) // 6

def squared_sum(n):
    return n * n * (n+1) * (n+1) // 4

print(squared_sum(100) - sum_of_squares(100))
