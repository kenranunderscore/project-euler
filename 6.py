def sumOfSquares(n):
    return int(n * (n+1) * (2*n+1) / 6)

def squareOfSum(n):
    return int(n * n * (n+1) * (n+1) / 4)

print(squareOfSum(100) - sumOfSquares(100))
