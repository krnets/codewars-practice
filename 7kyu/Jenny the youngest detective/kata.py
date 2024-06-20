# def missing(nums, s):
#     letters = "".join(s.split())
#     res = ""
#     for i in sorted(nums):
#         if i > len(letters) - 1:
#             return "No mission today"
#         res += letters[i]
#     return res.lower()


def missing(nums, s):
    letters = "".join(s.lower().split())
    if max(nums) >= len(letters):
        return "No mission today"
    return "".join(letters[i] for i in sorted(nums))
