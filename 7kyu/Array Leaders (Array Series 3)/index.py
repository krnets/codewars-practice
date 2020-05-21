# 7kyu - Array Leaders (Array Series #3)

""" Definition: An element is leader if it is greater than The Sum all the elements to its right side.

Given an array/list [] of integers, find all the LEADERS in the array.
    Array/list size is at least 3.
    Array/list's numbers Will be mixture of positives , negatives and zeros
    Repetition of numbers in the array/list could occur.
    Returned Array/list should store the leading numbers in the same order in the original array/list .

Input >> Output Examples

arrayLeaders ({1, 2, 3, 4, 0}) ==> return {4}
    4 is greater than the sum all the elements to its right side
    Note : The last element 0 is equal to right sum of its elements (abstract zero).

arrayLeaders ({16, 17, 4, 3, 5, 2}) ==> return {17, 5, 2}
    17 is greater than the sum all the elements to its right side
    5 is greater than the sum all the elements to its right side
    Note : The last element 2 is greater than the sum of its right elements (abstract zero).

arrayLeaders ({5, 2, -1}) ==> return {5, 2}
    5 is greater than the sum all the elements to its right side
    2 is greater than the sum all the elements to its right side
    Note : The last element -1 is less than the sum of its right elements (abstract zero).

arrayLeaders ({0, -1, -29, 3, 2}) ==> return {0, -1, 3, 2}
    0 is greater than the sum all the elements to its right side
    -1 is greater than the sum all the elements to its right side
    3 is greater than the sum all the elements to its right side
    Note : The last element 2 is greater than the sum of its right elements (abstract zero). """


# def array_leaders(numbers):
#     res = []
#     for i in range(len(numbers)):
#         if numbers[i] > sum(numbers[i+1:]):
#             res.append(numbers[i])
#     return res

# def array_leaders(numbers):     # inefficient due to sum being recalculated each time
#     return [n for (i, n) in enumerate(numbers) if n > sum(numbers[i+1:])]

def array_leaders(numbers):
    res = []
    s = 0
    for n in reversed(numbers):
        if n > s:
            res.append(n)
        s += n
    return res[::-1]

# def array_leaders(numbers):
#     res = []
#     s = sum(numbers)
#     for n in numbers:
#         s -= n
#         if(n > s):
#             res.append(n)
#     return res


# Test.it("Positive Values")
q = array_leaders([1, 2, 3, 4, 0])  # [4]
q
q = array_leaders([16, 17, 4, 3, 5, 2])  # [17,5,2]
q

# Test.it("Negative Values")
q = array_leaders([-1, -29, -26, -2])  # [-1]
q
q = array_leaders([-36, -12, -27])  # [-36,-12]
q

# Test.it("Mixed Values")
q = array_leaders([5, 2])  # [5,2]
q
q = array_leaders([0, -1, -29, 3, 2])  # [0,-1,3,2]
q
