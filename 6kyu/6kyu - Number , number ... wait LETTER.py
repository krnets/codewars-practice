# 6kyu - Number , number ... wait LETTER !

""" Your task is to write a function named do_math that receives a single argument. 
This argument is a string that contains multiple whitespace delimited numbers. 
Each number has a single alphabet letter somewhere within it.

Example : "24z6 1x23 y369 89a 900b"

As shown above, this alphabet letter can appear anywhere within the number. 
You have to extract the letters and sort the numbers according to their corresponding letters.

Example : "24z6 1x23 y369 89a 900b" will become 89 900 123 369 246 (ordered according to the alphabet letter)

Here comes the difficult part, now you have to do a series of computations on the numbers you have extracted.

    The sequence of computations are + - * /. 
    Basic math rules do NOT apply, you have to do each computation in exactly this order.
    This has to work for any size of numbers sent in (after division, go back to addition, etc).
    In the case of duplicate alphabet letters, you have to arrange them according to the number 
    that appeared first in the input string.
    Remember to also round the final answer to the nearest integer.

Examples :
"24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299
"24z6 1z23 y369 89z 900b" = 900 + 369 - 246 * 123 / 89 = 1414
"10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60 """

# import re

# def do_math(s):
#     sep = [(re.findall('\D', x)[0], re.sub('\D', '', x)) for x in s.split()]
#     nums = [x[1] for x in sorted(sep, key=lambda xs: xs[0])]
#     acc = nums[0]
#     operations = '+-*/'
#     for i in range(1, len(nums)):
#         acc = eval(f'{acc}{operations[(i-1)%4]}{nums[i]}')
#     return round(float(acc))


from re import fullmatch
from itertools import cycle
from functools import reduce
from operator import add, sub, mul, truediv as div

def do_math(s):
    sep = [fullmatch('(\d*)([a-z]+)(\d*)', x).groups() for x in s.split()]
    nums = [int(a + c) for a, _, c in sorted(sep, key=lambda x: x[1])]
    operation = cycle([add, sub, mul, div])
    return round(reduce(lambda a, b: next(operation)(a, b), nums))


q = do_math("24z6 1z23 y369 89z 900b"), 1414
q
q = do_math("24z6 1x23 y369 89a 900b"), 1299
q
q = do_math("10a 90x 14b 78u 45a 7b 34y"), 60
q
q = do_math("111a 222c 444y 777u 999a 888p"), 1459
q
q = do_math("1z 2t 3q 5x 6u 8a 7b"), 8
q
