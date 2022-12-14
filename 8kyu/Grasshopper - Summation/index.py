# 8kyu - Grasshopper - Summation

""" Write a program that finds the summation of every number from 1 to num. 
The number will always be a positive integer greater than 0. """


# def summation(num):
#     sum = 0
#     while num > 0:
#         sum += num
#         num -= 1
#     return sum

# def summation(num):
#     return (1 + num) * num / 2

# def summation(num):
#     return sum(range(num + 1))

# def summation(num):
#     return sum(range(num+1))

def summation(num):
    return num * (num + 1) // 2

q = summation(2)  # 3  (1 + 2)
q
q = summation(8)  # 36  (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
q
q = summation(1)  # 1
q
q = summation(8)  # 36
q
q = summation(22)  # 253
q
q = summation(100)  # 5050
q
q = summation(213)  # 22791
q
