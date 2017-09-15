words = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100:"one hundred",
    200:"two hundred",
    300:"three hundred",
    400:"four hundred",
    500:"five hundred",
    600:"six hundred",
    700:"seven hundred",
    800:"eight hundred",
    900:"nine hundred",
}

def translate(n):
    if n == 1000:
        return "one thousand"
    m = n % 100
    hundreds = n - m
    h = words[hundreds]
    if m == 0 and hundreds > 0:
        return h
    if hundreds > 0:
        h += " and "
    if m <= 20:
        return h + words[m]
    else:
        ones = n % 10
        tens = n - hundreds - ones
        return h + words[tens] + " " + words[ones]

translations = map(translate, range(1, 1001))
lengths = [len(t.replace(" ", "")) for t in translations]
print(sum(lengths))