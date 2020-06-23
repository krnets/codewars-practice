""" 7kyu - Fruit Ninja I

You are a Fruit Ninja, your skill is cutting fruit. All the fruit will be cut in half by your knife. For example:

[  "apple",     "pear",     "banana"  ]  -->
["app", "le", "pe", "ar", "ban", "ana"]

As you see, all fruits are cut in half. You should pay attention to "apple":
if you cannot cut a fruit into equal parts, then the first part will has a extra character.

You should only cut the fruit, other things should not be cut, such as the "bomb":

[  "apple",     "pear",     "banana",   "bomb"]  -->
["app", "le", "pe", "ar", "ban", "ana", "bomb"]

The valid fruit names are preloded for you as FRUIT_NAMES

Complete function cut_fruits that accepts argument fruits. Returns the result in accordance with the rules above."""


FRUIT_NAMES = {'coconut', 'pineapple', 'tomato', 'ginkgo', 'peach', 'plum', 'jujube', 'carambola',
               'cantaloupe', 'lemon', 'fig', 'mango', 'apple', 'blueberry', 'apricot', 'orange',
               'litchi', 'persimmon', 'hawthorn', 'pitaya', 'watermelon', 'grape', 'pomegranate',
               'cherry', 'banana', 'pear', 'durian', 'mangosteen'}


# def cut_fruits(fruits):
#     res = []
#     for x in fruits:
#         mid = (len(x)+1) // 2
#         if x in FRUIT_NAMES:
#             res.append(x[:mid])
#             res.append(x[mid:])
#         else:
#             res.append(x)
#     return res

def cut(x):
    if x in FRUIT_NAMES:
        mid = (len(x)+1) // 2
        return x[:mid], x[mid:]
    return [x]


def cut_fruits(fruits):
    return [x for xs in map(cut, fruits) for x in xs]


q = cut_fruits(["apple", "pear", "banana"])
q
# ["app", "le", "pe", "ar", "ban", "ana"]

q = cut_fruits(["apple", "pear", "banana", "bomb"])
q
# ["app", "le", "pe", "ar", "ban", "ana", "bomb"]
