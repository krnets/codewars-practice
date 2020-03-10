# 7kyu - Minimum Steps (Array Series #6)

""" Given an array of N integers, you have to find how many times you have to add up the smallest numbers in the array
until their Sum becomes greater or equal to K.

    List size is at least 3.
    All numbers will be positive.
    Numbers could occur more than once , (Duplications may exist).
    Threshold K will always be reachable.

Input >> Output Examples

minimumSteps({1, 10, 12, 9, 2, 3}, 6)  ==>  return (2)
    We add two smallest elements (1 + 2), their sum is 3 .
    Then we add the next smallest number to it (3 + 3) , so the sum becomes 6 .
    Now the result is greater or equal to 6 , Hence the output is (2) i.e (2) operations are required to do this .

minimumSteps({8 , 9, 4, 2}, 23)  ==> return (3)
    We add two smallest elements (4 + 2), their sum is 6 .
    Then we add the next smallest number to it (6 + 8) , so the sum becomes 14 .
    Now we add the next smallest number (14 + 9) , so the sum becomes 23 .
    Now the result is greater or equal to 23 , Hence the output is (3) i.e (3) operations are required to do this .

minimumSteps({19,98,69,28,75,45,17,98,67}, 464)  ==>  return (8)
    We add two smallest elements (19 + 17), their sum is 36 .
    Then we add the next smallest number to it (36 + 28) , so the sum becomes 64 .
    We need to keep doing this until the sum becomes greater or equal to K (464 in this case), which will require 8 Steps .

Expected Time Complexity
O(n Log n) """


# def minimum_steps(numbers, value):
#     numbers.sort()
#     acc = 0
#     count = 0
#     for i in range(len(numbers) - 1):
#         acc += numbers[i]
#         count += 1
#         if acc >= value:
#             return count - 1
#     return count

# def minimum_steps(numbers, value):
#     arr = sorted(numbers)
#     s = 0
#     for i, v in enumerate(arr):
#         s += v
#         if s >= value:
#             return i

from itertools import accumulate

def minimum_steps(numbers, value):
    return next(i for i, s in enumerate(accumulate(sorted(numbers))) if s >= value)


q = minimum_steps([4, 6, 3], 7)  # 1
q
q = minimum_steps([10, 9, 9, 8], 17)  # 1
q
q = minimum_steps([8, 9, 10, 4, 2], 23)  # 3
q
q = minimum_steps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464)  # 8
q
q = minimum_steps([4, 6, 3], 2)  # 0
q
