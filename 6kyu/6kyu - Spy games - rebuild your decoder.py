# 6kyu - Spy games - rebuild your decoder

""" You're operating behind enemy lines, but your decryption device took a bullet and no longer operates. 
You need to write a code to unscramble the encrypted messages coming in from headquarters. 
Luckily, you remember how the encryption algorithm works.

Each message you receive is a single string, with the blocks for each letter separated by a space. 
The blocks encoding the characters are made up of seemingly random characters and are of a variable length. 
For example, a two character word might look like:

"x20*6<xY y_r9L"

To decode this string, you add up only the numbers in each block:

sum of integers in "x20*6<xY" --> 2 + 0 + 6 = 8
sum of integers in "y_r9L" --> 9

Then map these numbers to the corresponding letters of the alphabet, with 0 representing a space:

0  : ' '
1  : 'a'
2  : 'b'
...
26 : 'z'

So we have:

"x20*6<xY y_r9L" --> "8 9" --> "hi"

Note also, if the sum of the digits goes over 26, loop back to zero 
(standard modulo / remainder function, such that 27 == 0, 28 == 1, etc.). 
As such the previous code could have also been:

"x20*6<xY y875_r97L" --> "8 36" --> "8 9" --> "hi" """

# import re

# def decrypt(code):
#     aa = [re.sub(r'\D+', '', x) for x in code.split()]
#     bb = [sum(int(y) for y in list(x)) for x in aa]
#     cc = [x % 27 if x > 26 else x for x in bb]
#     return ''.join(chr(x + 96) if x > 0 else ' ' for x in cc)

# def decrypt(code):
#     nums = [sum(int(i) for i in s if i.isdigit()) for s in code.split()]
#     wrap = [x % 27 if x > 26 else x for x in nums]
#     return ''.join(chr(x + 96) if x > 0 else ' ' for x in wrap)

# def decrypt(code):
#     return ''.join(' abcdefghijklmnopqrstuvwxyz'[sum(int(c) for c in w if c.isdigit()) % 27] for w in code.split())

# def decrypt(code):
#     abc = [' '] + list(map(chr, range(ord('a'), ord('z') + 1)))
#     return ''.join(abc[sum(int(c) for c in w if c.isdigit()) % 27] for w in code.split())

# def decrypt(code):
#     nums = [sum(map(int, filter(str.isdigit, x))) % 27 for x in code.split()]
#     return ''.join(chr(x + 96) if x else ' ' for x in nums)

def decrypt(code):
    return ''.join(chr(x + 96) if x else ' ' for x in (sum(map(int, filter(str.isdigit, x))) % 27 for x in code.split()))


q = decrypt('x20*6<xY y875_r97L')  # 'hi'
q
q = decrypt('8S6 K00= 3Ob28W4')  # 'n q'
q
