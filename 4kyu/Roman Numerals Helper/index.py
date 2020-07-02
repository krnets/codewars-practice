""" 4kyu - Roman Numerals Helper

Create a RomanNumerals class that can convert a roman numeral to and from an integer value. 
It should follow the API demonstrated in the examples below. 
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting 
with the left most digit and skipping any digit with a value of zero. 

In Roman numerals 1990 is rendered: 
1000=M, 900=CM, 90=XC resulting in MCMXC

2008 is written as 2000=MM, 8=VIII; or MMVIII

1666 uses each Roman symbol in descending order: MDCLXVI

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

| Symbol | Value | |----------------| | I | 1 | | V | 5 | | X | 10 | | L | 50 | | C | 100 | | D | 500 | | M | 1000 | """


# class RomanNumerals():
#     @staticmethod
#     def to_roman(year):
#         ROMAN = 'M CM D CD C XC L XL X IX V IV I'.split()
#         NUMS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         out = ''
#         for r, num in zip(ROMAN, NUMS):
#             num, year = divmod(year, num)
#             out += r * num
#         return out

# @staticmethod
# def from_roman(roman):
#     vals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#     out = 0
#     for i in range(len(roman)):
#         if i < len(roman)-1 and vals[roman[i]] < vals[roman[i+1]]:
#             out -= vals[roman[i]]
#         else:
#             out += vals[roman[i]]
#     return out


class RomanNumerals(object):
    ROMAN = 'M CM D CD C XC L XL X IX V IV I'.split()
    NUMS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    @classmethod
    def to_roman(cls, year):
        out = ''
        for r, num in zip(cls.ROMAN, cls.NUMS):
            num, year = divmod(year, num)
            out += r * num
        return out

    @classmethod
    def from_roman(cls, roman):
        vals = dict(zip(cls.ROMAN, cls.NUMS))
        out = 0
        for i in range(len(roman)):
            if i < len(roman)-1 and vals[roman[i]] < vals[roman[i+1]]:
                out -= vals[roman[i]]
            else:
                out += vals[roman[i]]
        return out


q = RomanNumerals.to_roman(1000), 'M'
q
q = RomanNumerals.to_roman(1990), 'MCMXC'
q
q = RomanNumerals.from_roman('XXI'), 21
q
q = RomanNumerals.from_roman('MMVIII'), 2008
q
