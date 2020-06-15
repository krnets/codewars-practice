""" 7kyu - Mobile Display Keystrokes

Do you remember the old mobile display keyboards? Do you also remember how inconvenient it was to write on it?
Well, here you have to calculate how much keystrokes you have to do for a specific word.

This is the layout:

1      2 abc  3 def
4 ghi  5 jkl  6 mno
7 pqrs 8 tuv  9 wxyz
*      0      #

Return the amount of keystrokes of input str (! only letters, digits and special characters in lowercase included in layout without whitespaces !)

e.g:

mobileKeyboard("123") => 3 (1+1+1)
mobileKeyboard("abc") => 9 (2+3+4)
mobileKeyboard("codewars") => 26 (4+4+2+3+2+2+4+5) """

# KEY_MAP = {'0123456789*#': 1, 'adgjmptw': 2, 'behknqux': 3, 'cfilorvy': 4, 'sz': 5}

# def mobile_keyboard(s):
#     return sum(KEY_MAP[k] for c in s for k in KEY_MAP.keys() if c in k)

# KEY_PRESSES = ['0123456789*#', 'adgjmptw', 'behknqux', 'cfilorvy', 'sz']

# def mobile_keyboard(s):
#     return sum(i+1 for c in s for i, k in enumerate(KEY_PRESSES) if c in k)


def mobile_keyboard(s):
    return sum(-~'abc  def  ghi  jkl  mno  pqrs tuv  wxyz'.find(c) % 5+1 for c in s)


q = mobile_keyboard(""), 0
q
q = mobile_keyboard("123"), 3
q
q = mobile_keyboard("codewars"), 26
q
q = mobile_keyboard("zruf"), 16
q
q = mobile_keyboard("thisisasms"), 37
q
q = mobile_keyboard("longwordwhichdontreallymakessense"), 107
q
