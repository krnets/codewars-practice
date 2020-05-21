# 7kyu - Letterbox Paint-Squad

""" You and a group of friends are earning some extra money in the school holidays by re-painting the numbers 
on people's letterboxes for a small fee.

Since there are 10 of you in the group each person just concentrates on painting one digit! 
For example, somebody will paint only the 1's, somebody else will paint only the 2's and so on...

But at the end of the day you realise not everybody did the same amount of work.

To avoid any fights you need to distribute the money fairly. That's where this Kata comes in.
Kata Task

Given the start and end letterbox numbers, write a method to return the frequency of all 10 digits painted.
Example

For start = 125, and end = 132

The letterboxes are

    125 = 1, 2, 5
    126 = 1, 2, 6
    127 = 1, 2, 7
    128 = 1, 2, 8
    129 = 1, 2, 9
    130 = 1, 3, 0
    131 = 1, 3, 1
    132 = 1, 3, 2

The digit frequencies are 1 x 0, 9 x 1, 6 x 2 etc...

and so the method would return [1,9,6,3,0,1,1,1,1,1]
Notes

    0 < start <= end
    In C, the returned value will be free'd. """

# from collections import Counter

# def paint_letterboxes(start, finish):
#     digits = ''.join(str(x) for x in list(range(start, finish + 1)))
#     index_count = Counter(range(10))
#     for i in range(len(index_count)):
#         index_count[i] = 0
#     for x in digits:
#         index_count[int(x)] += 1
#     return list(index_count.values())


# def paint_letterboxes(start, finish):
#     digits = ''.join(str(x) for x in range(start, finish + 1))
#     index_count = [0] * 10
#     for x in digits:
#         index_count[int(x)] += 1
#     return index_count

def paint_letterboxes(start, finish):
    digits = str(list(range(start, finish + 1)))
    return [digits.count(str(n)) for n in range(10)]


q = paint_letterboxes(125, 132)
q
# [1,9,6,3,0,1,1,1,1,1]
