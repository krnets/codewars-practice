# buttons = [" 0", "*", "#", "1", "ABC2", "DEF3", "GHI4", "JKL5", "MNO6", "PQRS7", "TUV8", "WXYZ9"]


# def presses(phrase):
#     ans = 0
#     for c in phrase.upper():
#         for key in KEYPAD:
#             if c in key:
#                 ans += key.index(c) + 1
#                 break
#     return ans

from collections import defaultdict

buttons = [" 0", "*", "#", "1", "ABC2", "DEF3", "GHI4", "JKL5", "MNO6", "PQRS7", "TUV8", "WXYZ9"]
KEYPAD = defaultdict(list)

for button in buttons:
    for i, c in enumerate(button, 1):
        KEYPAD[i].append(c)

VALS = {c: k for k, v in KEYPAD.items() for c in v}

def presses(phrase):
    return sum(map(VALS.get, phrase.upper()))
