# 7kyu - Regex validate PIN code

""" ATM machines allow 4 or 6 digit PIN codes.
PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False """

# import re

# def validate_pin(pin):
#     return bool(re.fullmatch(r'^(\d{4}|\d{6})$', pin))

# def validate_pin(pin):
#     return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


# "should return False for pins with length other than 4 or 6"
q = validate_pin('1234')  # False
q
q = validate_pin('098765')  # False
q
q = validate_pin("1")  # False
q
q = validate_pin("12")  # False
q
q = validate_pin("123")  # False
q
q = validate_pin("12345")  # False
q
q = validate_pin("1234567")  # False
q
q = validate_pin("-1234")  # False
q
q = validate_pin("1.234")  # False
q
q = validate_pin("-1.234")  # False
q
q = validate_pin("00000000")  # False
q

# "should return False for pins which contain characters other than digits"
q = validate_pin("a234")  # False
q
q = validate_pin(".234")  # False
q
q = validate_pin("-123")  # False
q
q = validate_pin("-1.234")  # False
q

# "should return True for valid pins"
q = validate_pin("1234")  # True
q
q = validate_pin("0000")  # True
q
q = validate_pin("1111")  # True
q
q = validate_pin("123456")  # True
q
q = validate_pin("098765")  # True
q
q = validate_pin("000000")  # True
q
q = validate_pin("123456")  # True
q
q = validate_pin("090909")  # True
q
