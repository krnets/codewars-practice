# 7kyu - sort array by last character

""" Write a function sort_me to sort a given array or list by last character of elements.

Element can be an integer or a string.

sortMe(['acvd','bcc']) => ['bcc','acvd']

The last characters of the strings are d and c. As c comes before d, sorting by last character will give ['bcc', 'acvd'].

If two elements don't differ in the last character, then they should be sorted by the order they come in the array. """


# def sort_me(arr):
#     return [x[0] for x in sorted(map(lambda x: [x, str(x)], arr), key=lambda x: x[1][-1])]

def sort_me(arr):
    return sorted(arr, key=lambda x: str(x)[-1])


q = sort_me(['acvd', 'bcc'])  # ['bcc','acvd']
q
q = sort_me(["asdf", 14, "13", "asdf"])  # ["13", 14, "asdf", "asdf"]
q
