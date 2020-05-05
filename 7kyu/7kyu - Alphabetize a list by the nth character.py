# 7kyu - Alphabetize a list by the nth character

""" Write a function that accepts two parameters: a string (containing a list of words) and an integer (n). 
The function should alphabetize the list based on the nth letter of each word.

The letters should be compared case-insensitive. 
If both letters are the same, order them normally (lexicographically), again, case-insensitive.

sortIt('bid, zag', 2) #=> 'zag, bid'

The length of all words provided in the list will be >= n. 
The format will be "x, x, x".  """

# from operator import itemgetter

# def sort_it(lst, n):
#     return ', '.join(sorted(lst.split(', '), key=itemgetter(n-1)))


def sort_it(lst, n):
    return ', '.join(sorted(lst.split(', '), key=lambda x: x[n-1]))


q = sort_it('bill, bell, ball, bull', 2), 'ball, bell, bill, bull'
q
q = sort_it('cat, dog, eel, bee', 3), 'bee, dog, eel, cat'
q
