""" 7kyu - Numbers to Letters

Given an array of numbers, you must return a string. 
The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. 
You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.

All inputs will be valid. """


def switcher(arr): return ''.join(
    (c > 26 and '!? '[c-27]) or chr(123-c) for c in map(int, arr) if c)


q = switcher(['24', '12', '23', '22', '4', '26', '9', '8'])  # 'codewars'
q
q = switcher(['25', '7', '8', '4', '14', '23', '8', '25',
              '23', '29', '16', '16', '4'])  # 'btswmdsbd kkw'
q
q = switcher(['4', '24'])  # 'wc'
q
q = switcher([20, 24, 20, 12, 22, 27, 7, 7, 19, 29, 14, 23, 21,
              17, 28, 25, 25, 8, 14, 12, 13])  # gcgoe!tth mdfj?bbsmon
q
