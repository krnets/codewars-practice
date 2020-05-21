# 7kyu - Are the numbers in order?

""" In this Kata, your function receives an array of integers as input. 
Your task is to determine whether the numbers are in ascending order. 
An array is said to be in ascending order if there are no two adjacent integers 
where the left integer exceeds the right integer in value.

For the purposes of this Kata, you may assume that all inputs are valid, 
i.e. non-empty arrays containing only integers.

Note that an array of 1 integer is automatically considered to be sorted 
in ascending order since all (zero) adjacent pairs of integers satisfy 
the condition that the left integer does not exceed the right integer in value. 
An empty list is considered a degenerate case and therefore will not be tested 

For example:

in_asc_order([1,2,4,7,19]) # returns True
in_asc_order([1,2,3,4,5]); // returns True
in_asc_order([1,6,10,18,2,4,20]) # returns False
in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order

N.B. If your solution passes all fixed tests but fails at the random tests, 
make sure you aren't mutating the input array. """


def in_asc_order(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# def in_asc_order(arr):
#     return arr == sorted(arr)

# def in_asc_order(arr):
#     return all(x < y for x, y in zip(arr, arr[1:]))


# Array of 2 integers
arr = [1, 2]
q = in_asc_order(arr)  # True
q

arr = [2, 1]
q = in_asc_order(arr)  # False
q

# Array of 3 integers
arr = [1, 2, 3]
q = in_asc_order(arr)  # True
q

arr = [1, 3, 2]
q = in_asc_order(arr)  # False
q

# More complex cases
arr = [1, 4, 13, 97, 508, 1047, 20058]
q = in_asc_order(arr)  # True
q

arr = [56, 98, 123, 67, 742, 1024, 32, 90969]
q = in_asc_order(arr)  # False
q
