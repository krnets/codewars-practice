# 6kyu - Numbers of Letters of Numbers

""" If we write out the digits of "60" as English words we get "sixzero";
the number of letters in "sixzero" is seven.
The number of letters in "seven" is five.
The number of letters in "five" is four.
The number of letters in "four" is four:
we have reached a stable equilibrium.

Note: for integers larger than 9, write out the names of each digit
in a single word (instead of the proper name of the number in English).
For example, write 12 as "onetwo" (instead of twelve),
and 999 as "nineninenine" (instead of nine hundred and ninety-nine).

For any integer between 0 and 999,
return an array showing the path from that integer to a stable equilibrium:

e.g. numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]
e.g. numbersOfLetters(1) --> ["one", "three", "five", "four"] """

# DIGITS = 'zero one two three four five six seven eight nine'.split()
# DIGITS_dict = {index: word for index, word in enumerate(DIGITS)}

# def numbers_of_letters(n):
#     out = []
#     cmp = ''.join(DIGITS_dict.get(int(x)) for x in str(n))
#     while len(DIGITS_dict.get(n, '')) != n:
#         out.append(cmp)
#         n = len(cmp)
#         cmp = ''.join(DIGITS_dict.get(int(x))
#                       for x in str(n)) if len(cmp) > 9 else DIGITS[len(cmp)]
#     out.append(cmp)
#     return out

# numbers_of_letters = f = lambda n, N=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]: (
#     lambda s: [s]+f(len(s))if len(s) != n else[s])(''.join(N[i]for i in map(int, str(n))))

# numbers_of_letters = f = lambda n, N='zero one two three four five six seven eight nine'.split(): (
#     lambda s: [s]+f(len(s))if len(s) != n else[s])(''.join(N[i]for i in map(int, str(n))))

N = 'zero one two three four five six seven eight nine'.split()

# def numbers_of_letters(n):
#     return (lambda s: [s]+numbers_of_letters(len(s)) if len(s) != n else[s])(''.join(N[i]for i in map(int, str(n))))

def numbers_of_letters(n):
    s = ''.join(N[i]for i in map(int, str(n)))
    return [s] + numbers_of_letters(len(s)) if len(s) != n else [s]


q = numbers_of_letters(1)
q
#      ["one", "three", "five", "four"]
q = numbers_of_letters(12)
q
#      ["onetwo", "six", "three", "five", "four"]
q = numbers_of_letters(37)
q
#      ["threeseven", "onezero", "seven", "five", "four"]
q = numbers_of_letters(311)
q
#      ['threeoneone', 'oneone', 'six', 'three', 'five', 'four']
q = numbers_of_letters(999)
q
#      ["nineninenine", "onetwo", "six", "three", "five", "four"]
