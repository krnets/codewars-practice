# 7kyu - Left$ and Right$

""" Once upon a time, more precisely upon BASIC time, there were 2 functions named LEFT$ and RIGHT$ 
(I wrote them uppercase because it was the custom in those early years).

These functions let you read left(/right)-most characters of a string.

    use: LEFT$ (str, i) -> returns i left-most characters of str.

- eg:
A$="ABCDEFG":PRINT LEFT$(A$,3) - prints ABC

and RIGHT$ (str, i ), of course, returns i right-most characters of str.
So, your mission is...

...to write 2 functions left & right that will work as the BASIC ones did,... except :

    i may be a negative integer. In this case the function returns the whole string 
    but i right(/left)-most chars (respectively in left$(/right$) function).
    if i === 0 : returns an empty string;
    if no i is provided consider it should be 1 ( not zero ).
    if i is greater than str length : returns the whole str.
and
    if i is a string ( yes it can ) : returns part of str at left(/right) of i.
        returns left of first occurence of i
        returns right of last occurence of i"""

def left(string, i=1):
    i = string.index(i) if isinstance(i, str) else i
    return string[:i]

def right(string, i=1):
    i = string[::-1].index(i[::-1]) if isinstance(i, str) else i
    return string[-i:] if i else ''

text = 'Hello (not so) cruel World!'

q = left('Hello o o o  World', 5), 'Hello'
q
q = right('Hello o o o  World', 5), 'World'
q
q = left('Hello o o o  World', 1), 'H'
q
q = left(text, 5), 'Hello'
q
q = left(text, -22), 'Hello'
q
q = left(text, 1), 'H'
q
q = left(text), 'H'
q
q = left(text, 0), ''
q
q = left(text, 99), 'Hello (not so) cruel World!'
q

q = right(text, 6), 'World!'
q
q = right(text), '!'
q

# == with string as 2nd argument ==
q = left(text, 'o'), 'Hell'
q
q = right(text, 'o'), 'rld!'
q
q = left(text, ' '),  'Hello'  # -- string may be a space
q
