SCORES = {
    "A": 100,
    "B": 14,
    "C": 9,
    "D": 28,
    "E": 145,
    "F": 12,
    "G": 3,
    "H": 10,
    "I": 200,
    "J": 100,
    "K": 114,
    "L": 100,
    "M": 25,
    "N": 450,
    "O": 80,
    "P": 2,
    "Q": 12,
    "R": 400,
    "S": 113,
    "T": 405,
    "U": 11,
    "V": 10,
    "W": 10,
    "X": 3,
    "Y": 210,
    "Z": 23,
}


# def sexy_name(name):
#     total = sum(SCORES.get(c, 0) for c in name.upper())

#     if total <= 60: return "NOT TOO SEXY"
#     if 61 <= total <= 300: return "PRETTY SEXY"
#     if 301 <= total <= 599: return "VERY SEXY"
#     return "THE ULTIMATE SEXIEST"


def sexy_name(name):
    total = sum(SCORES.get(c, 0) for c in name.upper())
    arr = [total > 60, total > 300, total > 600]
    return ("NOT TOO SEXY", "PRETTY SEXY", "VERY SEXY", "THE ULTIMATE SEXIEST")[sum(arr)]
