greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

# def greek_comparator(lhs, rhs):
#     a = greek_alphabet.index(lhs)
#     b = greek_alphabet.index(rhs)

#     return -1 if a < b else 1 if a > b else 0


def greek_comparator(lhs, rhs):
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
