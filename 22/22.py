def worth(word):
    return sum([ord(c) - 64 for c in word])

with open("data") as f:
    names = sorted([x.strip('"') for x in f.read().split(",")])
    s = 0
    for i in range(len(names)):
        s += (i + 1) * worth(names[i])
    print(s)