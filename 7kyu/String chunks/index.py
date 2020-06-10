""" 7kyu - String chunks

Write a function that takes a string and a positive integer n, splits the string into parts of length n 
and returns them in an array. It is ok for the last element to have less than n characters.

If n is not a valid size (> 0) (or is absent), you should return an empty array.
If n is greater than the length of the string, you should return an array with the only element being the same string. """


# def string_chunk(string, n=0):
#     try:
#         return [string[i:i+n] for i in range(0, len(string), n)]
#     except:
#         return []

# def string_chunk(string, n=0):
#     return [string[i:i+n] for i in range(0, len(string), n)] if isinstance(n, int) and n > 0 else []

def string_chunk(string, n=0):
    if not isinstance(n, int) or n == 0:
        return []
    return [string[i:i+n] for i in range(0, len(string), n)]


q = string_chunk('codewars', 2), ['co', 'de', 'wa', 'rs']
q
q = string_chunk('thiskataeasy', 4), ['this', 'kata', 'easy']
q
q = string_chunk('hello world', 3), ['hel', 'lo ', 'wor', 'ld']
q
q = string_chunk('everlong', 100), ['everlong']
q
q = string_chunk('sunny day', 0), []
q
