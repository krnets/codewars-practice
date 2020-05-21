# 6kyu - What century is it?

""" Return the inputted numerical year in century format. 
For example 2014, would return 21st.

The input will always be a 4 digit string. So there is no need for year string validation """


def whatCentury(year):
    century = str(1 + (int(year) - 1) // 100)
    suffix = {'1': 'st', '2': 'nd', '3': 'rd'}
    return century + 'th' if 3 < int(century) < 21 else century + suffix[century[-1]]


q = whatCentury(1999)  # 20th
q
q = whatCentury(2011)  # 21st
q
q = whatCentury(2154)  # 22nd
q
q = whatCentury(2259)  # 23rd
q
q = whatCentury(1124)  # 12th
q
q = whatCentury(2000)  # 20th
q
