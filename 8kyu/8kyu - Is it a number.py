# 8kyu - Is it a number?

""" Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

Valid examples, should return true:

isDigit("3")
isDigit("  3  ")
isDigit("-3.23")

should return false:

isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero") """

# def isDigit(string):
#     try: return bool(float(string)+1)
#     except: return False


def isDigit(string):
    try: return bool(float(string)) or True
    except: return False


q = isDigit("s2324")  # False
q
q = isDigit("-234.4")  # True
q
