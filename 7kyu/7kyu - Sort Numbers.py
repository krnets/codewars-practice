# 7kyu - Sort Numbers

""" Finish the solution so that it sorts the passed in array of numbers. 
If the function passes in an empty array or null value then it should return an empty array.


solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return [] """

# def solution(nums):
#     if nums is None:
#         return []
#     return sorted(nums)

# def solution(nums):
#     if not nums:
#         return []
#     return sorted(nums)

def solution(nums):
    return sorted(nums) if nums else []

# def solution(nums):
#     return sorted(nums or [])

q = solution([1, 2, 10, 5])  # [1,2,5,10]
q
