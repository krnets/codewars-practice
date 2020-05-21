# 8kyu - Removing Elements

""" Take an array and remove every second element out of that array. 
Always keep the first element and start removing with the next element.

Example:

my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]

None of the arrays will be empty, so you don't have to worry about that! """


# def remove_every_other(my_list):
#     res = []
#     for i in range(0, len(my_list)):
#         if i % 2 == 0:
#             res.append(my_list[i])
#     return res

def remove_every_other(my_list):
    return my_list[::2]


q = remove_every_other(['Hello', 'Goodbye', 'Hello Again'])
q
# ['Hello', 'Hello Again'])
q = remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # [1, 3, 5, 7, 9])
q
q = remove_every_other([[1, 2]])  # [[1, 2]]
q
q = remove_every_other([['Goodbye'], {'Great': 'Job'}])  # [['Goodbye']])
q
