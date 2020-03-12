# 7kyu - Descending Order

""" Your task is to make a function that can take any non-negative integer as a argument and 
return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.

Input: 21445 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321 """

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

q = descending_order(0)  # 0
q
q = descending_order(15)  # 51
q
q = descending_order(123456789)  # 987654321
q
