# 7kyu - Print count and numbers

""" Given a string of integers, count how many times that integer repeats itself, 
then return a string showing the count and the integer.

Example: count_me('1123')

    Here 1 comes twice so <count><integer> will be "21"
    then 2 comes once so <count><integer> will be "12"
    then 3 comes once so <count><integer> will be "13"

hence output string will be "211213".

Similarly count_me('211213') will return '1221121113' (1 time 2, 2 times 1, 1 time 2, 1 time 1, 1 time 3)

Return "" for empty, nil or non numeric strings """

# from re import search
# from itertools import groupby

# def count_me(data):
#     if not data or search(r'\D', data):
#         return ''
#     return ''.join((str(len(list(g))) + k) for k, g in groupby(data))

# from itertools import groupby

# def count_me(data):
#     return ''.join(str(len(list(g))) + k for k, g in groupby(data)) if data.isdigit() else ''

import re

def count_me(data):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), data) if data.isdigit() else ''


q = count_me('1123')  # '211213'
q
q = count_me('1')  # '11'
q
q = count_me('11')  # '21'
q
q = count_me('a')  # ''
q
q = count_me('a123')  # ''
q
q = count_me('21')  # '1211'
q
q = count_me('1211')  # '111221'
q
q = count_me('12322212223443')  # '111213321132132413'
q
q = count_me('')  # ''
q
q = count_me('123a')  # ''
q
