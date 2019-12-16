""" 6kyu - Roman Numerals Decoder

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC)
and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.  """


def solution(roman):
    vals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    for i in range(0, len(roman)):
        if i < len(roman)-1 and vals[roman[i]] < vals[roman[i+1]]:
            sum -= vals[roman[i]]
        else:
            sum += vals[roman[i]]
    return sum


q = solution('XXI')  # 21
q
q = solution('I')  # 1
q
q = solution('IV')  # 4
q
q = solution('MMVIII')  # 2008
q
q = solution('MDCLXVI')  # 1666
q
