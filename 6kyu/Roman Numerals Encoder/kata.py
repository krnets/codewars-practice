# def solution(n):
#     roman_numerals = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50),
#                       ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)]
#     res = ""
#     for roman, value in reversed(roman_numerals):
#         x = n // value
#         n -= x * value
#         res += roman * x
#     return res

def solution(n):
    roman_numerals = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50),
                      ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)]
    ans = ""
    for roman, value in reversed(roman_numerals):
        mult, n = divmod(n, value)
        ans += roman * mult
    return ans
