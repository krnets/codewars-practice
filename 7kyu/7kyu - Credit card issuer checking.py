""" 7kyu - Credit card issuer checking

 Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. 
If the number cannot be matched then the function should return the string Unknown.

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


def get_issuer(number):
    s = str(number)
    return ("AMEX"       if len(s) == 15 and s[:2] in ("34", "37") else
            "Discover"   if len(s) == 16 and s.startswith("6011") else
            "Mastercard" if len(s) == 16 and s[0] == "5" and s[1] in "12345" else
            "VISA"       if len(s) in [13, 16] and s[0] == "4" else "Unknown")


q = get_issuer(4111111111111111)  # 'VISA'
q
q = get_issuer(378282246310005)  # 'AMEX'
q
q = get_issuer(5105105105105100)  # "Mastercard"
q
q = get_issuer(9111111111111111)  # 'Unknown'
q
q = get_issuer(6011111111111117)  # "Discover"
q
