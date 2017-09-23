def triangle(n):
    return n * (n + 1) // 2

def char_val(c):
    return ord(c.upper()) - 64

def word_val(w):
    return sum([char_val(c) for c in w])

cache = [triangle(n) for n in range(1, 100)]

with open("data") as f:
    words = f.read().replace('"', '').split(",")
    triangle_words = [w for w in words if word_val(w) in cache]
    print(len(triangle_words))