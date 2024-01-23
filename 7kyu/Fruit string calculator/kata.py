import re


# def calculate(strng):
#     fst, op, snd = re.findall(r"\d+|gains|loses", strng)
#     return int(fst) + int(snd) if op == 'gains' else int(fst) - int(snd) if op == 'loses' else 0


def calculate(strng):
    fst, op, snd = re.findall(r"\d+|gains|loses", strng)
    match op:
        case "gains": return int(fst) + int(snd)
        case "loses": return int(fst) - int(snd)
