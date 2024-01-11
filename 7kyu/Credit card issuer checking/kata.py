# def get_issuer(number):
#     digits = str(number)

#     if len(digits) == 15 and digits[:2] in ("34", "37"):
#         return "AMEX"
#     if len(digits) == 16:
#         if digits[:4] == "6011":
#             return "Discover"
#         if int(digits[:2]) in (range(51, 56)):
#             return "Mastercard"
#         if digits[0] == "4":
#             return "VISA"
#     if len(digits) == 13 and digits[0] == "4":
#         return "VISA"

#     return "Unknown"


# | Card Type  | Begins With          | Number Length |
# |------------|----------------------|---------------|
# | AMEX       | 34 or 37             | 15            |
# | Discover   | 6011                 | 16            |
# | Mastercard | 51, 52, 53, 54 or 55 | 16            |
# | VISA       | 4                    | 13 or 16      |

import re

ISSUER = {
    'AMEX': r'3[47]\d{13}',
    'Discover': r'6011\d{12}',
    'Mastercard': r'5[1-5]\d{14}',
    'VISA': r'4\d{12}|4\d{15}' }

def get_issuer(number):
    digits = str(number)
    for key, pattern in ISSUER.items():
        if re.fullmatch(pattern, digits):
            return key
    return 'Unknown'


# def get_issuer(number):
#     n = number // 1e12

#     if n == 4: return "VISA"
#     if n == 6011: return "Discover"

#     n //= 10

#     if n in (34, 37): return "AMEX"
#     if 50 < n // 10 < 56: return "Mastercard"
#     return "VISA" if n // 100 == 4 else "Unknown"


# def get_issuer(number):
#     n = number // 1e12

#     match n:
#         case 4: return "VISA"
#         case 6011: return "Discover"

#     n //= 10

#     if n in (34, 37): return "AMEX"
#     if 50 < n // 10 < 56: return "Mastercard"

#     return "VISA" if n // 100 == 4 else "Unknown"
