import re

def testit(s):
    return len(re.findall(r"w.*?o.*?r.*?d.*?", s, re.I))
