# 6kyu - Dumbphone Keypads

""" Before smartphones and blackberry's without a qwerty keyboard, and prior to the development of 
T9 (predictive text entry) systems, the method to type words was called "multi-tap" and 
involved pressing a button repeatedly to cycle through the possible values.

------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |space| |     |
|  *  | |  0  | |  #  |
------- ------- -------

For example, to type a letter "R" you would press the 7 key three times (as the screen display 
for the current character cycles through P->Q->R->S->7). A character is "locked in" once the user presses 
a different key or pauses for a short period of time (thus, no extra button presses are required 
beyond what is needed for each letter individually). The zero key handles spaces, with one press 
of the key producing a space and two presses producing a zero.

For this assignment, write a module that can calculate the button presses sequence required for any phrase. 
Punctuation can be ignored for this exercise. Likewise, you can assume the phone doesn't distinguish 
between upper/lowercase characters (but you should allow your module to accept input in either for convenience).

For e.g. to type "HELLO WORLD", user would have to press the below sequence: 4433555p555666096667775553

p indicates a pause which is required before a character should get locked before the next character 
on the same key has to be pressed. In the above example, a pause is required before the keys can be 
pressed for the second instance of the character "L"

Try avoiding the obvious a-z combinations in order to support ease in change of Keypad combinations """


KEY_PRESSES = dict(A=2, B=22, C=222, D=3, E=33, F=333, G=4, H=44, I=444, J=5, K=55, L=555, M=6, N=66,
                   O=666, P=7, Q=77, R=777, S=7777, T=8, U=88, V=888, W=9, X=99, Y=999, Z=9999)

NUMS = {'0': '00', '1': '1', '2': '2222', '3': '3333', '4': '4444',
        '5': '5555', '6': '6666', '7': '77777', '8': '8888', '9': '99999'}

KEY_PRESSES.update(NUMS)


def sequence(phrase):
    res = ''
    for ch in phrase.upper():
        key = str(KEY_PRESSES.get(ch, ch))
        res += ('p' if res and key[0] == res[-1] else '') + key
    return res.replace(' ', '0')

# def sequence(phrase):
#     keypad = ['ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', ' 0']
#     res, prev = '', ''
#     for char in phrase.upper():
#         if char in '*#1':
#             res += ('p' if prev == char else '') + char
#             last = char
#         else:
#             for key in keypad:
#                 if char in key:
#                     res += ('p' if prev == key else '') + \
#                         (key.index(char)+1) * key[-1]
#                     last = key
#     return res

# from operator import itemgetter
# from itertools import groupby

# _LAYOUT = (' 0', '1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9')
# _KEYMAP = {c: str(i) * j for i, key in enumerate(_LAYOUT)  for j, c in enumerate(key, 1)}


# def sequence(phrase):
#     presses = (_KEYMAP.get(c.upper(), c) for c in phrase)
#     return ''.join('p'.join(group) for __, group in groupby(presses, key=itemgetter(0)))


q = sequence("HELLO WORLD"), "4433555p555666096667775553"
q
q = sequence("#hashtag"), "#442777744824"
q
q = sequence("yyuunn"), "4433555p555666096667775553"
q
