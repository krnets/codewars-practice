# def vert_mirror(strng):
#     return "\n".join(line[::-1] for line in strng.split())


# def hor_mirror(strng):
#     return "\n".join([*reversed(strng.split())])


# def oper(fct, s):
#     return fct(s)


def vert_mirror(strng):
    return [sub[::-1] for sub in strng]

def hor_mirror(strng):
    return strng[::-1]

def oper(fct, s):
    return "\n".join(map("".join, fct(s.split())))


# vertical
q = oper(vert_mirror, "abcd\nefgh\nijkl\nmnop")
q
#     dcba\nhgfe\nlkji\nponm
q = oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu")
q
#     QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw
q = oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx")
q
#     EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP

#  horizontal
q = oper(hor_mirror, "abcd\nefgh\nijkl\nmnop")
q
#     mnop\nijkl\nefgh\nabcd
q = oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt")
q
#     yeCt\nCSbg\nJVhv\nlVHt
q = oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz")
q
#     cEYz\nLPKo\ndbrZ\nnjMK
