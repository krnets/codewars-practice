# 7kyu - How many animals are there?

""" From a sentence, deduce the total number of animals.

"I see 3 zebras, 5 lions and 6 giraffes." The answer must be 14

"Mom, 3 rhinoceros and 6 snakes come to us!" The answer must be 9 """


# import re

# def count_animals(sentence):
#     return sum(int(x) for x in re.findall(r'(\d+)', sentence))

# def count_animals(sentence):
#     return sum(int(x) for x in re.findall(r'\d+', sentence))

# def count_animals(sentence):
#     return sum(map(int, re.findall(r'\d+', sentence)))

# def count_animals(sentence):
#     return sum(int(x) for x in sentence.split() if x.isdigit())

def count_animals(sentence):
    return sum(map(int, filter(str.isdigit, sentence.split())))


q = count_animals("I see 3 zebras, 5 lions and 6 giraffes.")  # 14
q
q = count_animals("Mom, 3 rhinoceros and 6 snakes come to us!")  # 9
q
q = count_animals("I do not see any animals here!")  # 0
q
q = count_animals("Mom, 38 rhinoceros and 116 snakes come to us!")  # 9
q
