# 7kyu - Mumbling

""" This time no story, no theory. The examples below show you how to write function accum:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z. """

# def accum(s):
#     return '-'.join( ''.join([x, x.lower() * i]) for i, x in enumerate(list(s.upper())))

# def accum(s):
#     return '-'.join( ''.join([x.upper(), x.lower() * i]) for i, x in enumerate(list(s)))


# def accum(s):
#     return '-'.join((c * i).title() for i, c in enumerate(s, 1))

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

q = accum("ZpglnRxqenU") # "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
q
q = accum("NyffsGeyylB") # "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
q
q = accum("MjtkuBovqrU") # "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
q
q = accum("EvidjUnokmM") # "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
q
q = accum("HbideVbxncC") # "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"
q