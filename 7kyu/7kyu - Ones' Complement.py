# 7kyu - Ones' Complement

""" The Ones' Complement of a binary number is the number obtained by swapping all the 0s for 1s and all the 1s for 0s. For example:

onesComplement(1001) = 0110
onesComplement(1001) = 0110

For any given binary number,formatted as a string, return the Ones' Complement of that number. """


def ones_complement(binary_number):
    return binary_number.translate(str.maketrans("01", "10"))


q = ones_complement("0")  # "1"
q
q = ones_complement("1")  # "0"
q
q = ones_complement("01")  # "10"
q
q = ones_complement("10")  # "01"
q
q = ones_complement("1101")  # "0010"
q
