# 6kyu - HTML Complementary Color

""" You have to implement the get_reversed_color(hex_color) function that takes a hex-color string and
returns the string represents the complementary color.

What is the hex-color? You can find the answer on w3schools and Wikipedia

Input
It takes only one argument - string with hex value (case-ignored with chars 0..9 or A..F) without hash-char "#".
Argument hex_color is not necessarily with 6-digits length - rest of digits are filled by zeros:

"a23" <=> "000a23"
"" <=> "0" <=> "000000"

Output
Output is the upper-cased string contains of the hash character (#) and complementary color.
Complementary color is some color which gives completely white color in sum with entered one:
# 000A23 + #FFF5DC = #FFFFFF

Errors
If the entered string is incorrect: length is 7+, has non-hexadecimal characters or non-string type,
then the Error(IllegalArgumentException - Java) should be raised/thrown.

>>> getReversedColor("00fffff")
Uncaught Error: Incorrect string length
>>> getReversedColor("00ffZZ")
Uncaught Error: Non-hex chars
>>> getReversedColor(112233)
Uncaught Error: Incorrect string type """


# import re

# def get_reversed_color(hex_color):
#     if hex_color == '0' or hex_color == '':
#         return '#FFFFFF'
#     if not (isinstance(hex_color, str)) or not re.match(r'^([a-fA-F\d]){0,6}$', hex_color):
#         raise Exception('Error')
#     try:
#         return '#' + (hex(int('FFFFFF', 16) - int(hex_color, 16))[2:]).upper()
#     except ValueError:
#         return 'Invalid value'

# def get_reversed_color(hex_color):
#     assert len(hex_color) < 7
#     return f"#{0xFFFFFF - int(hex_color or '0', 16):6X}"


def get_reversed_color(hex_color):
    assert len(hex_color) < 7
    return f"#{int(hex_color or '0', 16) ^ 0xFFFFFF:6X}"


q = get_reversed_color("FFFFFF")  # 0
q
q = get_reversed_color("01fD08")  # "#FE02F7"
q
q = get_reversed_color("")  # "#FFFFFF"
q
q = get_reversed_color("a23")  # "#FFF5DC"
q

q = get_reversed_color("")
q
# "#FFFFFF", "Result should begins with hash-char - #"

q = get_reversed_color("0")
q
# "#FFFFFF", "Result should begins with hash-char - #"

q = get_reversed_color("1234567")
q
# "Invalid length value should throw error."

q = get_reversed_color("AA00ZZ")
q
# "Invalid character in hex_color should throw error."

q = get_reversed_color(0)
q
# "Invalid type value should throw error."
