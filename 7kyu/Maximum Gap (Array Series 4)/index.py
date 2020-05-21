# 7kyu - Maximum Gap (Array Series #4)

""" Given an array/list [] of integers, find the maximum difference between the successive elements in its sorted form.

    Array/list size is at least 3 .
    Array/list's numbers Will be mixture of positives and negatives also zeros_
    Repetition of numbers in the array/list could occur.
    The Maximum Gap is computed Regardless the sign.

Input >> Output Examples

maxGap ({13,10,5,2,9}) ==> return (4)
    The Maximum Gap after sorting the array is 4 , The difference between 9 - 5 = 4 .

maxGap ({-3,-27,-4,-2}) ==> return (23)
    The Maximum Gap after sorting the array is 23 , The difference between |-4- (-27) | = 23 .
    Note : Regardless the sign of negativity .

maxGap ({-7,-42,-809,-14,-12}) ==> return (767)  
    The Maximum Gap after sorting the array is 767 , The difference between | -809- (-42) | = 767 .
    Note : Regardless the sign of negativity .

maxGap ({-54,37,0,64,640,0,-15}) //return (576)
    The Maximum Gap after sorting the array is 576 , The difference between | 64 - 640 | = 576 .
    Note : Regardless the sign of negativity . """


def max_gap(numbers):
    numbers.sort()
    return max(y - x for x, y in zip(numbers, numbers[1:]))

# from numpy import diff

# def max_gap(numbers):
#     return max(diff(sorted(numbers)))

q = max_gap([13, 10, 2, 9, 5])  # 4
q
q = max_gap([13, 3, 5])  # 8
q
q = max_gap([24, 299, 131, 14, 26, 25])  # 168
q
q = max_gap([-3, -27, -4, -2])  # 23
q
q = max_gap([-7, -42, -809, -14, -12])  # 767
q
q = max_gap([12, -5, -7, 0, 290])  # 278
q
q = max_gap([-54, 37, 0, 64, -15, 640, 0])  # 576
q
q = max_gap([130, 30, 50])  # 80
q
q = max_gap([1, 1, 1])  # 0
q
q = max_gap([-1, -1, -1])  # 0
q