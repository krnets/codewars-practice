# 7kyu - Smallest value of an array

""" Write a function that can return the smallest value of an array or the index of that value. 
The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates. 
Assume the second parameter will be a string holding one of two values: 'value' and 'index'.

min([1,2,3,4,5], 'value') // => 1
min([1,2,3,4,5], 'index') // => 0 """


# def find_smallest(numbers, to_return):
#     if to_return == 'value':
#         return min(numbers)
#     elif to_return == 'index':
#         return numbers.index(min(numbers))

# def find_smallest(numbers, to_return):
#     return min(numbers) if to_return == 'value' else numbers.index(min(numbers))

def find_smallest(numbers, to_return):
    val = min(numbers)
    return val if to_return == 'value' else numbers.index(val)


q = find_smallest([5, 4, 3, 2, 1], "value")  # 1
q
q = find_smallest([5, 4, 3, 2, 1], "index")  # 4
q
q = find_smallest([8, 0, 9], "index")  # 1
q
q = find_smallest([8, 0, 9], "value")  # 0
q
q = find_smallest([1, 1, 0, 0, 1, 1], "value")  # 0
q
q = find_smallest([1, 1, 0, 0, 1, 1], "index")  # 2
q
