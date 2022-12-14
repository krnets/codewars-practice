# 6kyu - Bit Counting

""" Write a function that takes an integer as input, and returns the number of bits that are equal 
to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case """


# def countBits(n):
#     return bin(n).count('1')


# def countBits(n):
#     ans = 0
#     while n:
#         ans += n % 2
#         n >>= 1
#     return ans


# def countBits(n):
#     return (n & 1) + countBits(n >> 1) if n else 0

countBits = int.bit_count


q = countBits(0)  # 0
q
q = countBits(4)  # 1
q
q = countBits(7)  # 3
q
q = countBits(9)  # 2
q
q = countBits(10)  # 2
q
q = countBits(11)
q
q = countBits(1024)
q
q = countBits(2048)
q
q = countBits(64)
q
