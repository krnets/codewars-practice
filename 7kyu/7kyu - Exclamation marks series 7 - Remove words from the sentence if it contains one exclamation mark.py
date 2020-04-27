# 7kyu - Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark

""" Remove words from the sentence if it contains one exclamation mark. 
Words are separated by spaces in the sentence. Please remember, one.

Examples

remove("Hi!") === ""
remove("Hi! Hi!") === ""
remove("Hi! Hi! Hi!") === ""
remove("Hi Hi! Hi!") === "Hi"
remove("Hi! !Hi Hi!") === ""
remove("Hi! Hi!! Hi!") === "Hi!!"
remove("Hi! !Hi! Hi!") === "!Hi!" """


def remove(s):
    return ' '.join(x for x in s.split() if x.count('!') != 1)


q = remove('Hi!')  # ''
q
q = remove('Hi!!!')  # 'Hi!!!'
q
q = remove('!Hi')  # ''
q
q = remove('!Hi!')  # '!Hi!'
q
q = remove('Hi! Hi!')  # ''
q
q = remove('!!!Hi !!hi!!! !hi')  # '!!!Hi !!hi!!!'
q
q = remove('!Hi! ! !Hi!')  # '!Hi! !Hi!'
q
