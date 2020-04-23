# 7kyu - "Center yourself", says the monk.

""" Your company MRE Tech has hired a spiritual consultant who advised on a new Balance policy: 
Don't take sides, don't favour, stay in the middle. This policy even applies to the software 
where all strings should now be centered. You are the poor soul to implement it.

Implement a function center that takes a string strng, an integer width, and an optional character 
fill (default: ' ') and returns a new string of length width where strng is centered and 
on the right and left padded with fill.

center(strng, width, fill=' ')

If the left and right padding cannot be of equal length make the padding on the left side one character longer.

If strng is longer than width return strng unchanged.

center('a', 3)  # returns " a "
center('abc', 10, '_')  # returns "____abc___"
center('abcdefg', 2)  # returns "abcdefg" """

# def center(strng, width, fill=' '):
#     width -= len(strng)
#     right = width // 2
#     left = width - right
#     return "{}{}{}".format(left * fill, strng, right * fill)

# def center(strng, width, fill=' '):
#     width -= len(strng)
#     right = width // 2
#     left = width - right
#     return left * fill + strng + right * fill

def center(strng, width, fill=' '):
    return fill * ((width + 1 - len(strng)) // 2) + strng + fill * ((width - len(strng)) // 2)


q = center('a', 4, '_'), '__a_'
q
q = center('', 2, '_'), '__'
q
q = center('a', 2, '_'), '_a'
q
q = center('a', 5, '_'), '__a__'
q
q = center('a', 3, '_'), '_a_'
q
q = center('ab', 3, '_'), '_ab'
q
q = center("a", 3), " a "
q
q = center("abc", 10, '_'), "____abc___"
q
q = center("abcdefg", 2), "abcdefg"
q
