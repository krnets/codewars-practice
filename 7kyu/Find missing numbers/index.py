# 7kyu - Find missing numbers

""" You will get an array of numbers.

Every preceding number is smaller than the one following it.

Some numbers will be missing, for instance:

[-3,-2,1,5] //missing numbers are: -1,0,2,3,4

Your task is to return an array of those missing numbers:

[-1,0,2,3,4] """


# def find_missing_numbers(arr):
#     try:
#         return [x for x in range(min(arr), max(arr)) if x not in arr]
#     except:
#         return []

def find_missing_numbers(arr):
    return [x for x in range(min(arr), max(arr)) if x not in arr] if arr else []


q = find_missing_numbers([-3, -2, 1, 4])  # [-1,0,2,3]
q
q = find_missing_numbers([-1, 0, 1, 2, 3, 4])  # []
q
q = find_missing_numbers([])  # []
q
q = find_missing_numbers([0])  # []
q
q = find_missing_numbers([-4, 4])  # [-3,-2,-1,0,1,2,3]
q
