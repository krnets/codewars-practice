# Beta - Two's complement

""" Two's complement is a mathematical operation on binary numbers.

You will be provided with a number, for test cases you can asumme it as to be always a non negative integer.

To solve the problem you need to convert the number to binary and invert it. 
At this point you'll have the one's complement. The two's complement it's the 1's plus 1.

Example:

step 1.- 45 to binary 101101; 
step 2.- 101101 inverted 010010 (one's complement); 
step 3.- 010010 inverted 010011 (two's complement); step 4.- 010011 to decimal 19

The tests expect the decimal conversion of that last complement. """


# def get_two_complement_int(n):
#     return 1 + int(bin(n)[2:].translate(str.maketrans("01", "10")), 2)

# def get_two_complement_int(n):
#     return 2 ** n.bit_length()
#     # return bin(n)[2:], n.bit_length(), 2 ** n.bit_length(), 2 ** n.bit_length() - n

def get_two_complement_int(n):
    return (n ^ (1 << n.bit_length())-1) + 1
    # return n, bin(n)[2:], n.bit_length(), bin((1 << n.bit_length()) - 1)[2:], bin(n ^ (1 << n.bit_length()) - 1)[2:], (n ^ (1 << n.bit_length()) - 1) + 1


q = get_two_complement_int(45)  # 19
q
q = get_two_complement_int(22)  # 10
q
q = get_two_complement_int(31)  # 1
q
q = get_two_complement_int(84)  # 44
q
q = get_two_complement_int(453)  # 59
q
q = get_two_complement_int(1001)  # 23
q
q = get_two_complement_int(10)  # 6
q
q = get_two_complement_int(1)  # 1
q
q = get_two_complement_int(2)  # 2
q
q = get_two_complement_int(3)  # 1
q
