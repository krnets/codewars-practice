""" 6kyu - Compress/Encode a Message with RLE (Run Length Encoding)

Run Length Encoding is used to compress data. RLE works like this: 
characters = "AAAALOTOOOOFTEEEEXXXXXXT" then the encoding will store AAAA = A4 and L1 So all together:

encode("AAAALOTOOOOFTEEEEXXXXXXT") == "A4L1O1T1O4F1T1E4X6T1"
# or
encode("HELLO WORLD") == "H1E1L2O1 1W1O1R1L1D1"
# or
encode("FOO+BAR") == "F1O2+1B1A1R1"

as you can see, its not always as efficient, but with some specific data it works! """

from itertools import groupby
# import re

# def encode(inp):
#     return ''.join(''.join([str(k), str(len(list(g)))]) for k, g in groupby(inp))

def encode(inp):
    return ''.join(k + str(len(list(g))) for k, g in groupby(inp))

# def encode(inp):
#     return ''.join(f'{c}{len(g)}' for g, c in re.findall(r'((.)\2*)', inp))


q = encode("HIIITTTTHEERRRR"), "H1I3T4H1E2R4"
q
