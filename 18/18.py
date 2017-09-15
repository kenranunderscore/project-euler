# assumes that the triangle isn't standing on its tip
def maximum_total(rows):
    for i in reversed(range(1, len(rows))):
        for j in range(len(rows[i]) - 1):
            m = max(rows[i][j], rows[i][j + 1])
            rows[i - 1][j] += m
    return rows[0][0]

rows = []
with open("data") as f:
    for line in f:
        rows.append([int(x) for x in line.split()])

print(maximum_total(rows))