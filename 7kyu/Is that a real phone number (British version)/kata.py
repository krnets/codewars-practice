import re

# def validate_number(st):
#     if re.fullmatch(r"(\+44|0)7\d{9}", st.replace("-", "")):
#         return "In with a chance"
#     return "Plenty more fish in the sea"


def validate_number(st):
    pattern = r"(?:-*)(\+44|0)7(?:\d-*){9}(?:-*)"
    if re.fullmatch(pattern, st):
        return "In with a chance"
    return "Plenty more fish in the sea"
