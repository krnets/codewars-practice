# 8kyu - Abbreviate a Two Word Name

""" Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:

Sam Harris => S.H
Patrick Feeney => P.F """

# def abbrevName(name):
#     [first, last] = name.split(' ')
#     return first[0].capitalize() + '.' + last[0].capitalize()

def abbrevName(name):
    return '.'.join(w[0] for w in name.split(' ')).upper()


q = abbrevName("Sam Harris")  # "S.H"
q
q = abbrevName("Patrick Feenan")  # "P.F"
q
q = abbrevName("Evan Cole")  # "E.C"
q
q = abbrevName("P Favuzzi")  # "P.F"
q
q = abbrevName("David Mendieta")  # "D.M"
q
