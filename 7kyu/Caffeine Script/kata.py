# 7kyu - Caffeine Script

""" Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.

If the integer is divisible by 3, return the string "Java".
If the integer is divisible by 3 and divisible by 4, return the string "Coffee"
If the integer is one of the above and is even, add "Script" to the end of the string.

Otherwise, return the string "mocha_missing!"""


# def caffeine_buzz(n):
#     return ("mocha_missing!", "Java", "JavaScript", "CoffeeScript")[sum([n % 4 == 0, n % 3 == 0, n % 2 == 0])]


# def caffeine_buzz(n):
#     if n % 3 == 0:
#         if n % 4 == 0:
#             return "Coffee" + ("Script", "")[n % 2]
#         return "Java" + ("Script", "")[n % 2]
#     return "mocha_missing!"


def caffeine_buzz(n):
    ans = ("", ("Java", "Coffee")[n % 4 == 0])[n % 3 == 0]
    return ans + "Script" * (n % 2 == 0) if ans else "mocha_missing!"



q = caffeine_buzz(1)  # "mocha_missing!"
q
q = caffeine_buzz(2)  # "mocha_missing!"
q
q = caffeine_buzz(3)  # "Java"
q
q = caffeine_buzz(4)  # "mocha_missing!"
q
q = caffeine_buzz(5)  # "mocha_missing!"
q
q = caffeine_buzz(6)  # "JavaScript"
q
q = caffeine_buzz(7)  # "mocha_missing!"
q
q = caffeine_buzz(8)  # "mocha_missing!"
q
q = caffeine_buzz(9)  # "Java"
q
q = caffeine_buzz(10)  # "mocha_missing!"
q
q = caffeine_buzz(11)  # "mocha_missing!"
q
q = caffeine_buzz(12)  # "CoffeeScript"
q
