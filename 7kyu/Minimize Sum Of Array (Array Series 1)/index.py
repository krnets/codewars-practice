# 7kyu - Minimize Sum Of Array (Array Series #1)

""" Given an array of integers, Find the minimum sum which is obtained from summing each Two integers product .

    Array/list will contain positives only.
    Array/list will always has even size

Input >> Output Examples

minSum({5,4,2,3}) ==> return (22) 

Explanation:

    The minimum sum obtained from summing each two integers product , 5*2 + 3*4 = 22

minSum({12,6,10,26,3,24}) ==> return (342)

Explanation:

    The minimum sum obtained from summing each two integers product , 26*3 + 24*6 + 12*10 = 342

minSum({9,2,8,7,5,4,0,6}) ==> return (74)

Explanation:

    The minimum sum obtained from summing each two integers product , 9*0 + 8*2 +7*4 +6*5 = 74 """


# def min_sum(arr):
#     sum = 0
#     arr = sorted(arr)
#     while len(arr) > 0:
#         sum += arr[0] * arr[-1]
#         arr = arr[1:-1]
#     return sum

def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i] * arr[-i-1] for i in range(len(arr) // 2))

# def min_sum(arr):
#     arr.sort()  # not the best practice, as it sorts array that may be used by another funciton elsewhere
#     return sum(arr[i] * arr[-i-1] for i in range(len(arr) // 2))


q = min_sum([5, 4, 2, 3])  # 22
q
q = min_sum([12, 6, 10, 26, 3, 24])  # 342
q
q = min_sum([9, 2, 8, 7, 5, 4, 0, 6])  # 74
q
