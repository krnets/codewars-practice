# 7kyu - Palindrome chain length

""" Number is a palindrome if it is equal to the number with digits in reversed order. 
For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.

Write a method palindrome_chain_length which takes a positive number and returns the number 
of special steps needed to obtain a palindrome. The special step is: "reverse the digits, 
and add to the original number". If the resulting number is not a palindrome, repeat the procedure 
with the sum until the resulting number is a palindrome.

If the input number is already a palindrome, the number of steps is 0.

Input will always be a positive integer.

For example, start with 87:

87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884

4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4 """

# def is_palindrome(x):
#     return str(x)[::-1] == str(x)

# def palindrome_chain_length(n):
#     steps = 0
#     while not is_palindrome(n):
#         steps += 1
#         n = int(str(n)[::-1]) + n
#     return steps

# def palindrome_chain_length(n):
#     steps = 0
#     while str(n)[::-1] != str(n):
#         steps += 1
#         n = int(str(n)[::-1]) + n
#     return steps

# def palindrome_chain_length(n):
#     steps = 0
#     while str(n) != str(n)[::-1]:
#         n = n + int(str(n)[::-1])
#         steps += 1
#     return steps

# def palindrome_chain_length(n, times=0):
#     reversed = int(str(n)[::-1])
#     if reversed == n:
#         return times
#     return palindrome_chain_length(n + reversed, times + 1)


# def palindrome_chain_length(n):
#     steps = 0

#     def is_palindrome(m):
#         s = str(m)
#         return s == s[::-1]

#     while not is_palindrome(n):
#         n += int(str(n)[::-1])
#         steps += 1

#     return steps


# def palindrome_chain_length(n):
#     steps = 0

#     while str(n) != (reversed_str_n := str(n)[::-1]):
#         n += int(reversed_str_n)
#         steps += 1

#     return steps


def palindrome_chain_length(n):
    steps = 0

    while (s := str(n)) != (reversed_str_n := s[::-1]):
        n += int(reversed_str_n)
        steps += 1

    return steps


q = palindrome_chain_length(87)  # 4
q
q = palindrome_chain_length(878)  # 0
q
