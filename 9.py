def find_pythagorean_triplet(sum):
    for a in range(1, sum):
        for b in range(1, sum - a):
            c = sum - a - b
            if a * a + b * b == c * c:
                return [a, b, c]
 
pt = find_pythagorean_triplet(1000)
print(str(pt[0] * pt[1] * pt[2]))
