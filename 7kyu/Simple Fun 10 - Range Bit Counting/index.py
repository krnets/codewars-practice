# 7kyu - Simple Fun #10: Range Bit Counting

""" You are given two numbers a and b where 0 ≤ a ≤ b. 
Imagine you construct an array of all the integers from a to b inclusive. 
You need to count the number of 1s in the binary representations of all the numbers in the array.

For a = 2 and b = 7, the output should be 11

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. 
Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], 
which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

    [input] integer a

    Constraints: 0 ≤ a ≤ b.
    [input] integer b

    Constraints: a ≤ b ≤ 100.
    [output] an integer """


# def range_bit_count(a, b):
# return ''.join(bin(x) for x in range(a, b + 1)).count('1')

def range_bit_count(a, b):
    return sum(bin(i).count('1') for i in range(a, b + 1))


q = range_bit_count(2, 7)  # 11
q
q = range_bit_count(0, 1)  # 1
q
q = range_bit_count(4, 4)  # 1
q
