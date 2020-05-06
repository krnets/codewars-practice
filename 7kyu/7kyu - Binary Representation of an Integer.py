# 7kyu - Binary Representation of an Integer

""" Write a function that returns a vector (list in Python) with each element representing one bit of a 
32bit unsigned/signed integer in such a way that if printed it would appear as the binary representation 
of the integer (Least Significant Bit on the right).

e.g. 1 = 00000000000000000000000000000001

Assign either a 1 or a 0 to the vector element depending on whether the bit at the corresponding position is a 1 or 0.

For example:

showBits(1); 

would return the following:

vector<int> bits = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};

-1 on the other hand would contain all 1s:

showBits(-1); 

vector<int> bits = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};

The function takes one argument (n) which is the integer to be converted to binary. """


# def showBits(n):
#     return [int(x) for x in '{:032b}'.format(n & 2**32-1)]

# def showBits(n):
#     return [int(x) for x in format(n & 2**32-1, '032b')]

def showBits(n):
    return list(map(int, format(n & 2**32-1, '032b')))


q = showBits(701)
q
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1]

q = showBits(-245)
q
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1]

q = showBits(12336)
q
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
