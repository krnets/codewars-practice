# 7kyu - Sort by Last Char

""" Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

If two words have the same last letter, they returned array should show them in the order they appeared in the given string.

All inputs will be valid. """

def last(x):
    return sorted(x.split(), key=lambda word: word[-1])

q = last("man i need a taxi up to ubud") # ["a", "need", "ubud", "i", "taxi", "man", "to", "up"]
q
q = last("what time are we climbing up the volcano") # ["time", "are", "we", "the", "climbing", "volcano", "up", "what"])
q
q = last("take me to semynak") # ["take", "me", "semynak", "to"]
q
q = last("massage yes massage yes massage") # ["massage", "massage", "massage", "yes", "yes"]
q
q = last("take bintang and a dance please") # ["a", "and", "take", "dance", "please", "bintang"]
q
