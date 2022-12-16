import re

def vaporcode(s):
    return "  ".join(map(str.upper, re.sub("\s", "", s)))


q = vaporcode("Lets go to the movies")
#  L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S
q
q = vaporcode("Why isn't my code working?")
#  W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?
q
