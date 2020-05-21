# 7kyu - Caffeine Script

""" Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.

If the integer is divisible by 3, return the string "Java".
If the integer is divisible by 3 and divisible by 4, return the string "Coffee"
If the integer is one of the above and is even, add "Script" to the end of the string.

Otherwise, return the string "mocha_missing!"""


# def caffeineBuzz(n):
#     res = ''
#     if n % 3 == 0 and n % 4 == 0:
#         res += 'Coffee'
#     elif n % 3 == 0:
#         res += 'Java'
#     if n % 2 == 0:
#         res += 'Script'
#     return res if res else 'mocha_missing!'

# def caffeineBuzz(n):
#     return ['mocha_missing!', 'Java', 'JavaScript', 'CoffeeScript'][sum([n % 4 == 0, n % 3 == 0, n % 2 == 0])]

def caffeineBuzz(n):
    return ['mocha_missing!', 'Java', 'Coffee'][(n % 4 == 0) + (n % 3 == 0)] + 'Script' * (n % 2 == 0)


q = caffeineBuzz(1)  # "mocha_missing!"
q
q = caffeineBuzz(3)  # "Java"
q
q = caffeineBuzz(6)  # "JavaScript"
q
q = caffeineBuzz(12)  # "CoffeeScript"
q
