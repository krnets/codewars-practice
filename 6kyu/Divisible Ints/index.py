# 6kyu - Divisible Ints

""" You are given an integer N. 
Your job is to figure out how many substrings inside of N divide evenly with N.

Confused? I'll break it down for you.

Let's say that you are given the integer '877692'.

8 does not evenly divide with 877692. 877692/8 = 109711 with 4 remainder.
7 does not evenly divide with 877692. 877692/7 = 125384 with 4 remainder.
7 does not evenly divide with 877692. 877692/7 = 125384 with 4 remainder.
6 evenly divides with 877692. 877692/6 = 146282 with 0 remainder.
9 does not evenly divide with 877692. 877692/9 = 97521 with 3 remainder.
2 evenly divides with 877692. 877692/2 = 438846 with 0 remainder.

We aren't going to stop there though. We need to check ALL of the substrings inside of 877692.

87 does not evenly divide with 877692. 877692/87 = 10088 with 36 remainder.
77 does not evenly divide with 877692. 877692/77 = 11398 with 46 remainder.
76 does not evenly divide with 877692. 877692/76 = 11548 with 44 remainder.
69 does not evenly divide with 877692. 877692/69 = 12720 with 12 remainder.

etc.

#Rules:
-If an integer is 0, then it does NOT divide evenly into anything.
-Even though N can divide evenly with itself, we do not count it towards the end number. For Example:

N = 23, the answer will be 0.  

-If there are multiple instances of a number, they all get counted. For example:

N = 11, the answer will be 2 

Input: A non negative integer.

Output: The number of times you found an integer that was evenly divisible with N. """

# def get_count(n):
#     str_n = str(n)
#     count = 0
#     for i in range(len(str_n)):
#         for j in range(i+1, len(str_n) + 1):
#             temp = int(str_n[i:j])
#             if temp != 0 and n % temp == 0:
#                 count += 1
#     return count - 1


def get_count(n):
    str_n = str(n)
    count = 0
    for i in range(1, len(str_n)):
        for j in range(len(str_n) - i + 1):
            temp = int(str_n[j:i+j])
            if temp and n % temp == 0:
                count += 1
    return count


q = get_count(877692)  # 2
q
q = get_count(11)  # 2
q
q = get_count(123)  # 2
q
q = get_count(1230)  # 5
q
q = get_count(1)  # 0
q
q = get_count(1111111111)  # 25
q
