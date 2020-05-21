# 7kyu - Numbers to Letters

""" Given an array of numbers (in string format), return a string. 
The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. 
You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.

All inputs will be valid. """

# from string import ascii_lowercase as abc

# def switcher(arr):
#     chars = abc[::-1] + '!? '
#     return ''.join(chars[int(x)-1] for x in arr)

# chars = abc[::-1] + '!? '

# def switcher(arr):
#     return ''.join(chars[int(x)-1] for x in arr if 0 < int(x) <= len(chars))


def switcher(arr):
    return ''.join({'27': '!', '28': '?', '29': ' '}.get(x, chr(26 - int(x) + ord('a'))) for x in arr)


q = switcher(['24', '12', '23', '22', '4', '26', '9', '8']), 'codewars'
q
q = switcher(['25', '7', '8', '4', '14', '23', '8', '25',
              '23', '29', '16', '16', '4']), 'btswmdsbd kkw'
q
q = switcher(['4', '24']), 'wc'
q
q = switcher(['12']), 'o'
q
q = switcher(['12', '28', '25', '21', '25', '7',
              '11', '22', '15']), 'o?bfbtpel'
q
