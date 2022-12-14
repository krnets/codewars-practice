# 6kyu - Stop gninnipS My sdroW!

""" Write a function that takes in a string of one or more words, and returns the same string, but with all 
five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of 
only letters and spaces. Spaces will be included only when more than one word is present."""


# def spin_words(sentence):
#     res = sentence.split(' ')
#     return ' '.join(map(lambda x: x[::-1] if len(x) >= 5 else x, res))

# def spin_words(sentence):
# return ' '.join(map(lambda x: x[::-1] if len(x) >= 5 else x, sentence.split(' ')))

# def spin_words(sentence):
#     return ' '.join(x[::-1] if len(x) >= 5 else x for x in sentence.split(' '))

# def spin_words(sentence):
#     return ' '.join(word if len(word) < 5 else word[::-1] for word in sentence.split(' '))

def spin_words(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())

q = spin_words("Welcome")  # "emocleW"
q
q = spin_words("Hey fellow warriors")  # "Hey wollef sroirraw"
q
q = spin_words("This is a test")  # "This is a test"
q
q = spin_words("This is another test")  # "This is rehtona test"
q
