# 7kyu - More than Zero?

""" Correct this code so that it takes one argument, x, and returns "x is more than zero" 
if x is positive (and nonzero), and otherwise, returns "x is equal to or less than zero." 

In both cases, replace x with the actual value of x. """


def corrections(x):
    return '{} is {} than zero.'.format(x, 'more' if x > 0 else 'equal to or less')


q = corrections(8), "8 is more than zero."
q
q = corrections(1), "1 is more than zero."
q
q = corrections(-2), "-2 is equal to or less than zero."
q
q = corrections(-1), "-1 is equal to or less than zero."
q
q = corrections(0), "0 is equal to or less than zero."
q
