def sumOfSquares(n):
    return n * (n+1) * (2*n+1) / 6

def squareOfSum(n):
    return n * n * (n+1) * (n+1) / 4

print(squareOfSum(100) - sumOfSquares(100))
