# 7kyu - Move 10

""" Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0. """

from string import ascii_lowercase as abc

# def move_ten(st):
#     return ''.join(abc[(abc.index(c)+10) % 26] for c in st)

def move_ten(st):
    table = str.maketrans(abc, abc[10:] + abc[:10])
    return st.translate(table)

# def move_ten(st):
#     a = abc + abc
#     return (''.join([a[a.find(i)+10] for i in st]))

q = move_ten("testcase"), "docdmkco"
q
q = move_ten("codewars"), "mynogkbc"
q
q = move_ten("exampletesthere"), "ohkwzvodocdrobo"
q
q = move_ten("returnofthespacecamel"), "bodebxypdroczkmomkwov"
q
q = move_ten("bringonthebootcamp"), "lbsxqyxdrolyydmkwz"
q
q = move_ten("weneedanofficedog"), "goxoonkxyppsmonyq"
q
