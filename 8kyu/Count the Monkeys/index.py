# 8kyu - Count the Monkeys!

""" You take your son to the forest to see the monkeys. You know that there are a certain number there (n), 
but your son is too young to just appreciate the full number, he has to start counting them from 1.

As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers 
up to and including that number, but excluding zero.

For example:

monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
monkeyCount(1) # --> [1] """


# def monkey_count(n):
#     res = []
#     while n:
#         res.append(n)
#         n -= 1
#     return list(reversed(res))

# def monkey_count(n):
#     res = []
#     for i in range(1, n + 1):
#         res.append(i)
#     return res

# def monkey_count(n):
#     return [i for i in range(1, n + 1)]

def monkey_count(n):
    return list(range(1, n + 1))


q = monkey_count(5)  # [1, 2, 3, 4, 5]
q
q = monkey_count(3)  # [1, 2, 3]
q
q = monkey_count(9)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
q
q = monkey_count(10)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
q
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
q = monkey_count(20)
q
