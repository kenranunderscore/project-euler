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
    90:"ninety"
}

def translate(n):
    if n == 1000:
        return "one thousand"
    hundreds = int(n / 100)
    m = n - 100 * hundreds
    if m == 0 and hundreds > 0:
        return words[hundreds] + " hundred"
    elif m <= 20:
        if hundreds > 0:
            return words[hundreds] + " hundred and " + words[m]
        else:
            return words[m]
    else:
        ones = n % 10
        tens = n - 100 * hundreds - ones
        if hundreds > 0:
            return words[hundreds] + " hundred and " + words[tens] + " " + words[ones]
        else:
            return words[tens] + " " + words[ones]

translations = map(translate, range(1, 1001))
lengths = [len(t.replace(" ", "")) for t in translations]
print(sum(lengths))