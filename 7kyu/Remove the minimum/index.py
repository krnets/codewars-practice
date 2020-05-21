# 7kyu - Remove the minimum

""" The museum of incredible dull things wants to get rid of some exhibitions. 
Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. 
She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair, 
so she asks you to write a program that tells her the ratings of the items 
after one removed the lowest one. Fair enough.

Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
If there are multiple elements with the same value, remove the one with a lower index. 
If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left. """


# def remove_smallest(numbers):
#     if not numbers:
#         return numbers
#     clone = numbers[::]
#     clone.remove(min(numbers))
#     return clone

# def remove_smallest(numbers):
#     clone = numbers[:]
#     if clone:
#         clone.remove(min(numbers))
#     return clone

# def remove_smallest(numbers):
#     if not numbers:
#         return numbers
#     idx = numbers.index(min(numbers))
#     return numbers[0:idx] + numbers[idx+1:]

def remove_smallest(nums):
    return nums[:nums.index(min(nums))] + nums[nums.index(min(nums)) + 1:] if nums else nums


q = remove_smallest([1, 2, 3, 4, 5])  # [2,3,4,5]
q
q = remove_smallest([5, 3, 2, 1, 4])  # [5,3,2,4]
q
q = remove_smallest([2, 2, 1, 2, 1])  # [2,2,2,1]
q
