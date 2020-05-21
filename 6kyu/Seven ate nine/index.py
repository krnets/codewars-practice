# 6kyu - Seven "ate" nine!

""" Seven is a hungry number and its favourite food is number 9. 
Whenever it spots 9 through the hoops of 8, it eats it! 
Well, not anymore, because you are going to help the 9 by locating that particular sequence (7,8,9) 
in an array of digits and tell 7 to come after 9 instead. 
Seven "ate" nine, no more! (If 9 is not in danger, just return the same array) """

# def hungry_seven(arr):
#     nums = str(arr).replace(', ', '')
#     while nums.find(r'789') > 0:
#         nums = nums.replace(r'789', '897')
#     return [int(x) for x in list(nums) if x.isdigit()]

def hungry_seven(arr):
    nums = ''.join(map(str, arr))
    while '789' in nums:
        nums = nums.replace('789', '897')
    return [int(x) for x in nums]


q = hungry_seven([7, 8, 9])  # [8,9,7]
q
q = hungry_seven([7, 7, 7, 8, 9])  # [8,9,7,7,7]
q
q = hungry_seven([8, 7, 8, 9, 8, 9, 7, 8])  # [8,8,9,8,9,7,7,8]
q
q = hungry_seven([8, 7, 8, 7, 9, 8])  # [8,7,8,7,9,8]
q
