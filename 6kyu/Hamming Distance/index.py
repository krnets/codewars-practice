""" 6kyu - Hamming Distance

The Hamming Distance is a measure of similarity between two strings of equal length. 
Complete the function so that it returns the number of positions where the input strings do not match.


You can assume that the two input strings are of equal length. """


# def hamming(a, b):
#     return sum(x != y for x, y in zip(a, b))

def hamming(a, b):
    return sum(map(str.__ne__, a, b))


q = hamming("I like turtles", "I like turkeys"), 3
q
q = hamming("Hello World", "Hello World"), 0
q
