# 8kyu - Add Length

""" What if we need the length of the words separated by a space to be added at the end of that same word 
and have it returned as an array?

add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]

Your task is to write a function that takes a string and returns an list with the length of each word added to each element .
Note: String will have at least one element; words will always be separated by a space. """


# def add_length(str):
#     res = []
#     for x in str.split():
#         res.append(f'{x} {len(x)}')
#     return res

def add_length(str):
    return [f'{word} {len(word)}' for word in str.split()]


q = add_length('apple ban')  # ["apple 5", "ban 3"]
q
q = add_length('you will win')  # ["you 3", "will 4", "win 3"]
q
q = add_length('you')  # ["you 3"]
q
q = add_length('y')  # ["y 1"]
q
