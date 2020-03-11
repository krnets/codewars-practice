# 7kyu - Array element parity

""" In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, 
except for one integer that is either only negative or only positive. Your task will be to find that integer.

solve[1,-1,2,-2,3] = 3  --> 3 only has a positive ocurrence.
solve([-3,1,2,3,-1,-4,-2]) = -4  --> -4 only has a negative occurence
solve([1,-1,2,-2,3,3]) = 3  --> the integer that is only positive or only negative my appear more than once. """


# def solve(arr):
#     for x in arr:
#         if -x not in arr:
#             return x

# def solve(arr):
#     return [x for x in arr if -x not in arr][0]

def solve(arr):
    return sum(set(arr))

q = solve([1, -1, 2, -2, 3])  # 3
q
q = solve([-3, 1, 2, 3, -1, -4, -2])  # -4
q
q = solve([1, -1, 2, -2, 3, 3])  # 3
q
q = solve([-110, 110, -38, -38, -62, 62, -38, -38, -38])  # -38
q
q = solve([-9, -105, -9, -9, -9, -9, 105])  # -9
q
