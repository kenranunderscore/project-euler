import itertools

perms = list(itertools.permutations("0123456789"))
print("".join(perms[999999]))