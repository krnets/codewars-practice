""" 7kyu - String Repetition without Function

Digital Cypher assigns to each letter of the alphabet unique number. For example:

 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9 10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
14 15 16 17 18 19 20 21 22 23 24 25 26

Instead of letters in encrypted word we write the corresponding number, eg. The word scout:

 s  c  o  u  t
19  3 15 21 20

Then we add to each obtained digit consecutive digits from the key. For example. In case of key equal to 1939 :

   s  c  o  u  t
  19  3 15 21 20
 + 1  9  3  9  1
 ---------------
  20 12 18 30 21

   m  a  s  t  e  r  p  i  e  c  e
  13  1 19 20  5 18 16  9  5  3  5
+  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  14 10 22 29  6 27 19 18  6  12 8

Task

Write a function that accepts str string and key number and returns an array of integers representing encoded str.

The str input string consists of lowercase characters only.
The key input number is a positive integer.

Encode("scout",1939);  ==>  [ 20, 12, 18, 30, 21]
Encode("masterpiece",1939);  ==>  [ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8] """

from string import ascii_lowercase as abc
from itertools import cycle


# def encode(message, key):
#     ch_idx = [abc.index(ch)+1 for ch in message]
#     return [int(x) + y for x, y in list(zip(cycle(str(key)), ch_idx))]

# def encode(message, key):
#     return [int(x) + abc.index(ch)+1 for x, ch in list(zip(cycle(str(key)), message))]

def encode(message, key):
    return [abc.index(m)+k+1 for m, k in zip(message, cycle(map(int, str(key))))]


q = encode("scout", 1939), [20, 12, 18, 30, 21]
q
q = encode("masterpiece", 1939), [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
q
