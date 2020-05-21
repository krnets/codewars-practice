# 7kyu - Sort array by string length

""" Write a function that takes an array of strings as an argument and returns a sorted array 
containing the same strings, ordered from shortest to longest.

For example, if this array were passed as an argument:
["Telescopes", "Glasses", "Eyes", "Monocles"]

Your function would return the following array:
["Eyes", "Glasses", "Monocles", "Telescopes"]

All of the strings in the array passed to your function will be different lengths, 
so you will not have to decide how to order multiple strings of the same length. """


def sort_by_length(arr):
    return sorted(arr, key=len)


q = sort_by_length(["beg", "life", "i", "to"])
q
#      ["i", "to", "beg", "life"]
q = sort_by_length(["", "moderately", "brains", "pizza"])
q
#      ["", "pizza", "brains", "moderately"]
q = sort_by_length(["longer", "longest", "short"])
q
#      ["short", "longer", "longest"]
q = sort_by_length(["dog", "food", "a", "of"])
q
#      ["a", "of", "dog", "food"]
q = sort_by_length(["", "dictionary", "eloquent", "bees"])
q
#      ["", "bees", "eloquent", "dictionary"]
q = sort_by_length(["a longer sentence", "the longest sentence", "a short sentence"])
q
#   ["a short sentence", "a longer sentence", "the longest sentence"]
