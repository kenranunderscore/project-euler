def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def number_of_paths(grid_size):
    k = factorial(grid_size)
    return factorial(2 * grid_size) // (k * k)

print(number_of_paths(20))