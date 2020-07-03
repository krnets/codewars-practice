""" 6kyu - Data compression using run-length encoding

Run-length encoding (RLE) is a very simple form of lossless data compression 
in which runs of data are stored as a single data value and count.

A simple form of RLE would encode the string "AAABBBCCCD" as "3A3B3C1D" meaning, 
first there are 3 A, then 3 B, then 3 C and last there is 1 D.

Your task is to write a RLE encoder and decoder using this technique. 
The texts to encode will always consist of only uppercase characters, no numbers. """

# from itertools import groupby
import re

# def encode(string):
#     return ''.join(str(len(list(g)))+k for k, g in groupby(string))

def encode(string):
    return ''.join(f'{len(g)}{c}' for g, c in re.findall(r'((.)\2*)', string))

def decode(string):
    return ''.join(int(n) * c for n, c in re.findall(r'(\d+)(\w)', string))

# def encode(string):
#     return re.sub(r'(\D)\1*', lambda m: str(len(m.group(0))) + m.group(1), string)

# def decode(string):
#     return re.sub(r'(\d+)(\D)', lambda m: int(m.group(1)) * m.group(2), string)


q = encode("A"), "1A"
q
q = encode("AAA"), "3A"
q
q = encode("AB"), "1A1B"
q
q = encode("AAABBBCCCA"), "3A3B3C1A"
q

q = decode("1A"), "A"
q
q = decode("3A"), "AAA"
q
q = decode("1A1B"), "AB"
q
q = decode("3A3B3C1A"), "AAABBBCCCA"
q
q = decode("10A1B"), "10A1B"
q

q = decode(encode("AAAAAAAAAAB")), "AAAAAAAAAAB"
q
q = decode(encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ")), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
q
q = encode(decode("10A1B")), "10A1B"
q
q = encode(decode("1A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z")
           ), "1A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z"
q
