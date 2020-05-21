# 7kyu - Find the capitals

""" Write a function that takes a single string (word) as argument. 
The function must return an ordered list containing the indexes of all capital letters in the string. """


# def capitals(word):
#     return [i for i, c in enumerate(word) if c.upper() == c]

def capitals(word):
    return [i for i, c in enumerate(word) if c.isupper()]


q = capitals('CodEWaRs')  # [0,3,4,6]
q
