# 7kyu - Number Of Occurrences

""" Write a functionthat returns the number of occurrences of an element in an array."""

def number_of_occurrences(element, sample):
    return sample.count(element)

sample = [0, 1, 2, 2, 3]
q = number_of_occurrences(0, sample) # 1
q
q = number_of_occurrences(4, sample) # 0
q
q = number_of_occurrences(2, sample) # 2
q
q = number_of_occurrences(3, sample) # 1 
q
