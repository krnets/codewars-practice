# 7kyu - Search for letters

""" Create a function which accepts one arbitrary string as an argument, and return a string of length 26.

The objective is to set each of the 26 characters of the output string to either '1' or '0' 
based on the fact whether the Nth letter of the alphabet is present in the input (independent of its case).

So if an 'a' or an 'A' appears anywhere in the input string (any number of times), set the first character 
of the output string to '1', otherwise to '0'. if 'b' or 'B' appears in the string, set the second character 
to '1', and so on for the rest of the alphabet.

For instance:

"a   **&  cZ"  =>  "10100000000000000000000001" """

from re import sub
from string import ascii_lowercase as abc

def change(st):
    res = sub('[^a-z]', '', st.lower())
    return ''.join('1' if x in res else '0' for x in abc)


q = change("a **&  bZ"), "11000000000000000000000001"
q
q = change('Abc e  $$  z'), "11101000000000000000000001"
q
q = change("!!a$%&RgTT"), "10000010000000000101000000"
q
q = change(""), "00000000000000000000000000","empty string should return 26 '0'"
q
q = change("abcdefghijklmnopqrstuvwxyz"), "11111111111111111111111111"
q
q = change("aaaaaaaaaaa"), "10000000000000000000000000"
q
q = change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd"), "00010111000000000001000010"
q
