""" 6kyu - Thue-Morse Sequence

Given a positive integer n, return first n dgits of Thue-Morse sequence, as a string (see examples).

Thue-Morse sequence is a binary sequence with 0 as the first element. 
The rest of the sequece is obtained by adding the Boolean (binary) complement of a group obtained so far.

For example:

0
01
0110
01101001
and so on...

alt

Ex.:

thue_morse(1);  #"0"
thue_morse(2);  #"01"
thue_morse(5);  #"01101"
thue_morse(10): #"0110100110"

    You don't need to test if n is valid - it will always be a positive integer.
    n will be between 1 and 10000 """


def thue_morse(n):
    return ''.join(str(bin(i).count('1') % 2) for i in range(n))


q = thue_morse(1), "0"
q
q = thue_morse(2), "01"
q
q = thue_morse(5), "01101"
q
q = thue_morse(10), "0110100110"
q
q = thue_morse(100), "0110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110"
q
