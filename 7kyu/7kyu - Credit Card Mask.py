# 7kyu - Credit Card Mask

""" Usually when you buy something, you're asked whether your credit card number, phone number or answer 
to your most secret question is still correct. However, since someone could look over your shoulder, 
you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!" """


# def maskify(cc):
#     return '#' * (len(cc) - 4) + cc[-4:] if len(cc) > 4 else cc

# def maskify(cc):
#     return '#' * (len(cc)-4) + cc[-4:]

def maskify(cc):
    return cc[-4:].rjust(len(cc), '#')


cc = ''
r = maskify(cc)
# "masking: {0}".format(cc)
q = "{0}  matches  {1}".format(cc, r)
q
q = r, cc
q

cc = '123'
r = maskify(cc)
# "masking: {0}".format(cc)
q = "{0}  matches  {1}".format(cc, r)
q
q = r, cc
q

cc = 'SF$SDfgsd2eA'
r = maskify(cc)
# "masking: {0}".format(cc)
q = "{0}  matches  {1}".format('########d2eA', r)
q
q = r, '########d2eA'
q
