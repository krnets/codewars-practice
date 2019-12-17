""" 7kyu - Double Sort

Simple enough this one - you will be given an array. The values in the array will either be numbers or strings, 
or a mix of both. You will not get an empty array, nor a sparse one.

Your job is to return a single array that has first the numbers sorted in ascending order, followed by the strings 
sorted in alphabetic order. The values must maintain their original type.

Note that numbers written as strings are strings and must be sorted with the other strings.
Fundamentals | Strings | Numbers | Arrays """


# def db_sort(a):
#     nums = [num for num in a if not isinstance(num, str)]
#     strs = [str for str in a if not isinstance(str, int)]
#     nums.sort()
#     strs.sort()
#     return nums + strs


def db_sort(arr):
    return sorted(arr, key=lambda x: (isinstance(x, str), x))

# def db_sort(arr):
    # return sorted([i for i in arr if isinstance(i, int)]) + sorted([s for s in arr if isinstance(s, str)])


q = db_sort([6, 2, 3, 4, 5])  # [2, 3, 4, 5, 6]
q
q = db_sort([14, 32, 3, 5, 5])  # [3, 5, 5, 14, 32]
q
q = db_sort([1, 2, 3, 4, 5])  # [1, 2, 3, 4, 5]
q
# [2,2,8,"Apple","Banana","Mango","Orange"]
q = db_sort(["Banana", "Orange", "Apple", "Mango", 8, 2, 2])
q
q = db_sort(["C", "W", "W", "W", 1, 2, 0])  # [0,1,2,"C","W","W","W"]
q
# [5,6,6,7,10,15,110,"!","2500","come","on"])
q = db_sort(['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6])
q
