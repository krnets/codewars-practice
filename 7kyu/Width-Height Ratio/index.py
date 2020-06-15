""" 7kyu - Width-Height Ratio

We all use 16:9, 16:10, 4:3 etc. ratios every day. 
Main task is to determine image ratio by its width and height dimensions.

Function should take width and height of an image and return a ratio string (ex."16:9"). 
If any of width or height entry is 0 function should throw an exception (or return Nothing). """


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)


def calculate_ratio(w, h):
    if w == 0 or h == 0:
        raise ValueError('no ratio possible')
    n = gcd(w, h)
    return f'{w//n}:{h//n}'

# from fractions import Fraction

# def calculate_ratio(w, h):
#     if w * h == 0:
#         raise ValueError('no ratio possible')
#     return '{0.numerator}:{0.denominator}'.format(Fraction(w, h))


q = calculate_ratio(1024, 768), "4:3"
q
q = calculate_ratio(1920, 1080), "16:9"
q
q = calculate_ratio(600, 800), "3:4"
q
q = calculate_ratio(600, 600), "1:1"
q
