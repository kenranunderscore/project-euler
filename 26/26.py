def recurring_cycle_length(d):
    if d % 2 == 0 or d % 5 == 0:
        # not technically correct, but suffices to solve the problem
        # these cases produce no longer cycles
        return 0
    n = 1
    r = 1
    length = 0
    while True:
        n = 10 * r
        r = n % d
        length += 1
        if r == 1:
            break
    return length

lengths = [recurring_cycle_length(d) for d in range(2, 1000)]
longest = max(lengths)
print(lengths.index(longest) + 2)