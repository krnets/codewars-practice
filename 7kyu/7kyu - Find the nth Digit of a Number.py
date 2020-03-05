# 7kyu - Find the nth Digit of a Number

""" Complete the function that takes two numbers as input, num and nth and return the nth digit of num (counting from right to left).
Note

    If num is negative, ignore its sign and treat it as a positive value
    If nth is not positive, return -1
    Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0

Examples

findDigit(5673, 4)     returns 5
findDigit(129, 2)      returns 2
findDigit(-2825, 3)    returns 8
findDigit(-456, 4)     returns 0
findDigit(0, 20)       returns 0
findDigit(65, 0)       returns -1
findDigit(24, -8)      returns -1 """


# def find_digit(num, nth):
#     s = list(str(abs(num)))[::-1]
#     for i in range(0, len(s)):
#         if i == nth - 1:
#             return int(s[i])
#     return -1 if nth <= 0 else 0

# def find_digit(num, nth):
#     if nth <= 0:
#         return -1
#     try:
#         return int(str(num).lstrip('-')[-nth])
#     except IndexError:
#         return 0

def find_digit(num, nth):
    if nth <= 0:
        return -1
    try:
        return int(str(abs(num))[-nth])
    except IndexError:
        return 0

# def find_digit(num, nth):
#     num = str(num)
#     if nth <= 0:
#         return -1
#     if nth > len(num):
#         return 0
#     return int(num[-nth])


q = find_digit(9611, 7)  # 0
q
q = find_digit(9740, 6)  # 0
q
q = find_digit(23080, 6)  # 0
q
q = find_digit(5673, 4)  # 5
q
q = find_digit(129, 2)  # 2
q
q = find_digit(-2825, 3)  # 8
q
q = find_digit(0, 20)  # 0
q
q = find_digit(65, 0)  # -1
q
q = find_digit(24, -8)  # -1
q
q = find_digit(-1234, 2)  # 3
q
q = find_digit(-5540, 1)  # 0
q
q = find_digit(678998, 0)  # -1
q
q = find_digit(-67854, -57)  # -1
q
q = find_digit(0, -3)  # -1
q
