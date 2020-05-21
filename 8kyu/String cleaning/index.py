# 8kyu - String cleaning

""" Your boss decided to save money by purchasing some cut-rate optical character recognition software 
for scanning in the text of old novels to your database. At first it seems to capture words okay, 
but you quickly notice that it throws in a lot of numbers at random places in the text. For example:

string_clean('! !') == '! !'
string_clean('123456789') == ''
string_clean('This looks5 grea8t!') == 'This looks great!'

Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. 
Your program will take in a string and clean out all numeric characters, and return a string with spacing and 
special characters ~#$%^&!@*():;"'.,? all intact. """

# import re

# def string_clean(s):
#     return re.sub('\d', '', s)


def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())


q = string_clean("")  # ""
q
q = string_clean("! !")  # "! !"
q
q = string_clean("123456789")  # ""
q
q = string_clean("(E3at m2e2!!)")  # "(Eat me!!)"
q
q = string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!")
q
# "Dsa cdsc csa!!! I Am cool!"
q = string_clean("A1 A1! AAA   3J4K5L@!!!")
q
# "A A! AAA   JKL@!!!"
q = string_clean("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@")
q
# "Adgre Asad! AAA fvfdvJKL@"
# "Addsadds A  $$sad! AAAe fKL@ "
q = string_clean("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 ")
q
q = string_clean("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 ")
q
# "Addsadds A  $$sa!d! A!A!Ae$ f## "
q = string_clean(
    "My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?")
q
# "My \"messy\" data issues! Will they ever, ever be solved?"
q
q = string_clean("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3")
q
# "Why can't we buy the good software? #cheapskates"
