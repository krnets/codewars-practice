# 7kyu - Converting integer to currency format

""" Write a function that takes an integer in input and outputs a string with currency format.

Integer in currency format is expressed by a string of number where every three characters are separated by comma.

For example:

123456 --> "123,456"

Input will always be an positive integer, so don't worry about type checking or negative/float values. """

import re

# def to_currency(price):
#     return ','.join(re.findall('\d{1,3}', str(price)[::-1]))[::-1]

def to_currency(price):
    return re.sub('(\d)(?=(\d{3})+$)', '\\1,', str(price))

# def to_currency(price):
#     return format(price, ',')

# def to_currency(price):
#     return f'{price:,}'


q = to_currency(123456), "123,456"
q
q = to_currency(1234), "1,234"
q
q = to_currency(123), "123"
q
q = to_currency(123456789012), "123,456,789,012"
q
