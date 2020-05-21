# 7kyu - Alternate capitalization

""" Given a string, capitalize the letters that occupy even indexes and odd indexes separately, 
and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces. """


# def capitalize(s):
#     even = ''.join(s[i].lower() if i % 2 else s[i].upper() for i in range(len(s)))
#     odd = ''.join(x.swapcase() for x in even)
#     return [even, odd]

# def capitalize(s):
#     res = ''.join(s[i].lower() if i % 2 else s[i].upper() for i in range(len(s)))
#     return [res, res.swapcase()]

def capitalize(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]


q = capitalize("abcdef")  # ['AbCdEf', 'aBcDeF']
q
q = capitalize("codewars")  # ['CoDeWaRs', 'cOdEwArS']
q
q = capitalize("abracadabra")  # ['AbRaCaDaBrA', 'aBrAcAdAbRa']
q
q = capitalize("codewarriors")  # ['CoDeWaRrIoRs', 'cOdEwArRiOrS']
q
