# 7kyu - How many consecutive numbers are needed?

""" Create the function consecutive(arr) that takes an array of integers and return the minimum number of integers 
needed to make the contents of arr consecutive from the lowest number to the highest number.

For example:
If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the array (5 and 7) 
to make it a consecutive array of numbers from 4 to 8. Numbers in arr will be unique. """


# def consecutive(arr):
#     return len(range(min(arr), max(arr) + 1)) - len(arr) if arr else 0

def consecutive(arr):
    return max(arr) - min(arr) - len(arr) + 1 if arr else 0


q = consecutive([4, 8, 6])  # 2
q
q = consecutive([1, 2, 3, 4])  # 0
q
q = consecutive([])  # 0
q
q = consecutive([1])  # 0
q
q = consecutive([-10])  # 0
q
