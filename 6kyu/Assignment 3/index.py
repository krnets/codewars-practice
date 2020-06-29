""" 6kyu - Assignment #3

Third day at your new cryptoanalyst job and you come across your toughest assignment yet. 
Your job is to implement a simple keyword cipher. A keyword cipher is a type of 
monoalphabetic substitution where two parameters are provided as such (string, keyword). 
The string is encrypted by taking the keyword, dropping any letters that appear more than once. 
The rest of the letters of the alphabet that aren't used are then appended to the end of the keyword.

For example, if your string was "hello" and your keyword was "wednesday", 
your encryption key would be 'wednsaybcfghijklmopqrtuvxz'.

To encrypt 'hello' you'd substitute as follows,

              abcdefghijklmnopqrstuvwxyz
  hello ==>   |||||||||||||||||||||||||| ==> bshhk
              wednsaybcfghijklmopqrtuvxz

hello encrypts into bshhk with the keyword wednesday. This cipher also uses lower case letters only. """

from string import ascii_lowercase as abc

# def keyword_cipher(msg, keyword):
#     dedup = []
#     for x in keyword:
#         if x not in dedup:
#             dedup.append(x)
#     cipher = ''.join(dedup + [x for x in abc if x not in keyword])
#     return msg.lower().translate(str.maketrans(abc, cipher))


def keyword_cipher(msg, keyword, cipher=''):
    for c in keyword + abc:
        if c not in cipher:
            cipher += c
    return msg.lower().translate(str.maketrans(abc, cipher))


q = keyword_cipher("Welcome home", "secret"), "wticljt dljt"
q
q = keyword_cipher("hello", "wednesday"), "bshhk"
q
q = keyword_cipher("HELLO", "wednesday"), "bshhk"
q
q = keyword_cipher("HeLlO", "wednesday"), "bshhk"
q
q = keyword_cipher("WELCOME HOME", "gridlocked"), "wlfimhl kmhl"
q
q = keyword_cipher("alpha bravo charlie", "delta"), "djofd eqdvn lfdqjga"
q
q = keyword_cipher("Home Base", "seven"), "dlja esqa"
q
q = keyword_cipher("basecamp", "covert"), "ocprvcil"
q
q = keyword_cipher("one two three", "rails"), "mks twm tdpss"
q
q = keyword_cipher("Test", "unbuntu"), "raqr"
q
