# 7kyu - Offspring Traits

""" A population of bears consists of black bears, brown bears, and white bears.

The input is an array of two elements.

Determine whether the offspring of the two bears will 
return 'black', 'brown', 'white', 'dark brown', 'grey', 'light brown', or 'unknown'.

Elements in the the array will always be a string. """


def bear_fur(bears):
    a, b = sorted(bears)
    joined = f'{a} {b}'
    mix = {'black brown': 'dark brown', 'black white': 'grey', 'brown white': 'light brown'}
    if a == b:
        return a
    elif joined in mix:
        return mix[joined]
    else:
        return 'unknown'


q = bear_fur(['black', 'black'])  # 'black'
q
q = bear_fur(['brown', 'brown'])  # 'brown'
q
q = bear_fur(['white', 'white'])  # 'white'
q
q = bear_fur(['black', 'brown'])  # 'dark brown'
q
q = bear_fur(['black', 'white'])  # 'grey'
q
q = bear_fur(['brown', 'white'])  # 'light brown'
q
q = bear_fur(['yellow', 'magenta'])  # 'unknown'
q
