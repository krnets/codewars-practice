""" 7kyu - Algorithmic predicament- Bug Fixing #9

Oh no! Timmy's algorithim has gone wrong! help Timmy fix his algorithim!
Your task is to fix timmy's algorithim so it returns the group name with the highest total age.

You will receive two groups of people objects, with two properties name and age. 
The name property is a string and the age property is a number.

Your goal is to make the total the age of all people having the same name through both groups 
and return the name of the one with the highest age. 
If two names have the same total age return the first alphabetical name. """


# from collections import defaultdict


# def highest_age(group1, group2):
#     max_age = 0
#     max_names = []
#     total = defaultdict(int)
#     for person in group1 + group2:
#         name = person['name']
#         total[name] += person['age']
#         name_total = total[name]
#         if name_total > max_age:
#             max_age = name_total
#             max_names = [name]
#         elif name_total == max_age:
#             max_names.append(name)
#     return min(max_names)

from collections import defaultdict
from itertools import chain

def highest_age(group1, group2):
    total = defaultdict(int)
    for person in chain(group1, group2):
        total[person['name']] += person['age']
    return min(total, key=lambda p: (-total[p], p))


q = highest_age([{'name': 'kay', 'age': 1}, {'name': 'john', 'age': 13}, {'name': 'kay', 'age': 76}],
                [{'name': 'john', 'age': 1}, {'name': 'alice', 'age': 77}]), 'alice'
q
q = highest_age([{'name': 'kay', 'age': 1}, {'name': 'john', 'age': 13}, {'name': 'kay', 'age': 76}],
                [{'name': 'john', 'age': 1}, {'name': 'alice', 'age': 76}]), 'kay'
q
q = highest_age([{'name': 'kay', 'age': 1}, {'name': 'john', 'age': 130}, {'name': 'kay', 'age': 76}],
                [{'name': 'john', 'age': 1}, {'name': 'alice', 'age': 76}]), 'john'
q
q = highest_age([{'name': 'kay', 'age': 1}, {'name': 'john', 'age': 130}, {'name': 'kay', 'age': 130}],
                [{'name': 'john', 'age': 1}, {'name': 'alice', 'age': 76}]), 'john'
q
q = highest_age([{'name': 'kay', 'age': 2}, {'name': 'john', 'age': 130}, {'name': 'kay', 'age': 130}],
                [{'name': 'john', 'age': 1}, {'name': 'alice', 'age': 76}]), 'kay'
q
