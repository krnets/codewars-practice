# 7kyu - Credit card issuer checking
""" 
Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

Complete the function get_issuer() that will use the values shown below to determine the card issuer 
for a given card number. If the number cannot be matched then the function should return the string Unknown.

| Card Type  | Begins With          | Number Length |
|------------|----------------------|---------------|
| AMEX       | 34 or 37             | 15            |
| Discover   | 6011                 | 16            |
| Mastercard | 51, 52, 53, 54 or 55 | 16            |
| VISA       | 4                    | 13 or 16      | 

Examples

get_issuer(4111111111111111) == "VISA"
get_issuer(4111111111111) == "VISA"
get_issuer(4012888888881881) == "VISA"
get_issuer(378282246310005) == "AMEX"
get_issuer(6011111111111117) == "Discover"
get_issuer(5105105105105100) == "Mastercard"
get_issuer(5105105105105106) == "Mastercard"
get_issuer(9111111111111111) == "Unknown"  """


# def get_issuer(number):
#     s = str(number)
#     return ("AMEX"       if len(s) == 15 and s[:2] in ("34", "37") else
#             "Discover"   if len(s) == 16 and s.startswith("6011") else
#             "Mastercard" if len(s) == 16 and s[0] == "5" and s[1] in "12345" else
#             "VISA"       if len(s) in [13, 16] and s[0] == "4" else "Unknown")

# import re

# def get_issuer(number):
#     num = str(number)
#     if bool(re.match(r'^3[4|7]\d{13}$', num)):
#         return 'AMEX'
#     if bool(re.match(r'^4(\d{12}|\d{15})$', num)):
#         return 'VISA'
#     if bool(re.match(r'^5[1-5]\d{14}$', num)):
#         return 'Mastercard'
#     if bool(re.match(r'^6011\d{12}$', num)):
#         return 'Discover'
#     return 'Unknown'

VENDORS = [
    # Name         Begins with    Length
    ['AMEX',       (34, 37),      (15,)],
    ['Discover',   (6011,),       (16,)],
    ['Mastercard', range(51, 56), (16,)],
    ['VISA',       (4,),          (13, 16)],
]

def get_issuer(number):
    return next((
        vendor[0] for vendor in VENDORS
        if len(str(number)) in vendor[2] and any(str(number).startswith(str(start)) for start in vendor[1])
    ), 'Unknown')


q = get_issuer(4111111111111111)  # "VISA"
q
q = get_issuer(4111111111111)  # "VISA"
q
q = get_issuer(4012888888881881)  # "VISA"
q
q = get_issuer(378282246310005)  # "AMEX"
q
q = get_issuer(6011111111111117)  # "Discover"
q
q = get_issuer(5105105105105100)  # "Mastercard"
q
q = get_issuer(5105105105105106)  # "Mastercard"
q
q = get_issuer(9111111111111111)  # "Unknown"
q
