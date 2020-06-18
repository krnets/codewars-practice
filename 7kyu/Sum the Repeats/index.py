""" 7kyu - Sum the Repeats

Write a function that takes a list comprised of other lists of integers and returns the sum 
of all numbers that appear in two or more lists in the input list. 

Now that might have sounded confusing, it isn't:

repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
>> sum of [2, 8]
return 10

repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
>> sum of []
return 0

repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
sum of [1,8]
return 9 """

# from itertools import combinations

# def repeat_sum(l):
#     intersections = []
#     # for pair in combinations(l, 2):
#     #     intersections.append(set(pair[0]).intersection(set(pair[1])))
#     for x, y in combinations(l, 2):
#         intersections.append(set(x).intersection(set(y)))
#     try:
#         return sum(intersections[0].union(*intersections))
#     except IndexError:
#         return 0

# def repeat_sum(l):
#     common_vals = [set(x).intersection(set(y)) for x, y in combinations(l, 2)]
#     try:
#         return sum(common_vals[0].union(*common_vals))
#     except IndexError:
#         return 0


# from collections import defaultdict

# def repeat_sum(l):
#     count = defaultdict(int)
#     for sub in l:
#         for v in set(sub):
#             count[v] += 1

#     return sum(k for k, v in count.items() if v > 1)

from collections import Counter
# from itertools import chain

# def repeat_sum(l):
#     count = Counter(chain.from_iterable(set(x) for x in l))
#     return sum(k for k, v in count.items() if v > 1)


def repeat_sum(xs):
    count = Counter(y
                    for ys in xs
                    for y in set(ys))
    return sum(k for k, v in count.items() if v > 1)


q = repeat_sum([[1, 2, 3], [2, 8, 9], [7, 123, 8]]), 10
q
q = repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]), 0
q
q = repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]), 9
q
q = repeat_sum([[1]]), 0
q
