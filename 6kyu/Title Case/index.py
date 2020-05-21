# 6kyu - Title Case

""" A string is considered to be in title case if each word in the string is either (a) capitalised
(that is, only the first letter of the word is in upper case) or (b) considered to be an exception
and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions
(minor words). The list of minor words will be given as a string with each word separated by a space.
Your function should ignore the case of the minor words string -- it should behave in the same way
even if the case of the minor word string is changed.

Arguments

    First argument (required): the original string to be converted.
    Second argument (optional): space-delimited list of minor words that must always be lowercase
    except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

# should return: 'A Clash of Kings'
title_case('a clash of KINGS', 'a an the of')
# should return: 'The Wind in the Willows'
title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('the quick brown fox') # should return: 'The Quick Brown Fox' """

# def title_case(title, minor_words=''):
#     mw = list(map(str.lower, minor_words.split()))
#     words = map(str.lower, title.split())
#     out = ' '.join(x if x in mw else x.title() for x in words)
#     return out[0].upper() + out[1:] if out else out

# def title_case(title, minor_words=''):
#     ignored = list(map(str.lower, minor_words.split()))
#     words = map(str.lower, title.split())
#     out = ' '.join(x if x in ignored else x.capitalize() for x in words)
#     return out[0].upper() + out[1:] if out else out

# def title_case(title, minor_words=''):
#     title = title.capitalize().split()
#     minor_words = minor_words.lower().split()
#     return ' '.join(x if x in minor_words else x.capitalize() for x in title)

def title_case(title, minor_words=''):
    return ' '.join(x if x in minor_words.lower().split() else x.capitalize() for x in title.capitalize().split())


q = title_case('')  # ''
q
q = title_case('a clash of KINGS', 'a an the of')  # 'A Clash of Kings'
q
q = title_case('THE WIND IN THE WILLOWS', 'The In')
q
#     'The Wind in the Willows'
q = title_case('the quick brown fox')
q
#     'The Quick Brown Fox'
q = title_case('the QUICK bRoWn fOX', minor_words='xyz fox quick the')
q
#     'The quick Brown fox'
