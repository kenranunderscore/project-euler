with open("data13.txt") as f:
    sum = 0
    for line in f:
        sum += int(line)
    s = str(sum)
    print(s)
    print(s[:10])