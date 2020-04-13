# 7kyu - Help Bob count letters and digits

""" Bob needs you to create a method that can determine how many letters and digits are in a given string.

"hel2!lo" --> 6
"wicked .. !" --> 6
"!?..A" --> 1 """

# def count_letters_and_digits(s):
#     return sum(1 for x in s if x.isalpha() or x.isdigit())

# def count_letters_and_digits(s):
#     return sum(1 for x in s if x.isalnum())

def count_letters_and_digits(s):
    return sum(map(str.isalnum, s))


q = count_letters_and_digits('n!!ice!!123')  # 7
q
q = count_letters_and_digits('de?=?=tttes!!t')  # 8
q
q = count_letters_and_digits('')  # 0
q
q = count_letters_and_digits('!@#$%^&`~.')  # 0
q
q = count_letters_and_digits('u_n_d_e_r__S_C_O_R_E')  # 10
q
