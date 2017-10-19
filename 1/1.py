def sum_of_multiples_of_3_or_5(threshold):
    result = 0
    for i in range(0, threshold):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


print(sum_of_multiples_of_3_or_5(1000))