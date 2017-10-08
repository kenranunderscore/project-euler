def corner_sum(circle_number):
    if circle_number == 0:
        return 1
    first_corner = 4 * circle_number ** 2 - 2 * circle_number + 1
    increment = 2 * circle_number
    return 4 * first_corner + 6 * increment

result = sum([corner_sum(n) for n in range(501)])
print(result)