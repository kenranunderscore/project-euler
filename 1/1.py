def sum_of_multiples_of_3_or_5(max):
    sum = 0
    for i in range(0, max):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(sum_of_multiples_of_3_or_5(1000))