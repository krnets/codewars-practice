""" 7kyu - Sort by binary ones

In this example you need to implement a function that sort a list of integers based on it's binary representation.

The rules are simple:

    sort the list based on the amount of 1's in the binary representation of each number.
    if two numbers have the same amount of 1's, the shorter string goes first. (ex: "11" goes before "101" when sorting 3 and 5 respectively)
    if the amount of 1's is same, lower decimal number goes first. (ex: 21 = "10101" and 25 = "11001", then 21 goes first as is lower)

    Input: [1,15,5,7,3]
        ( in binary strings is: ["1", "1111", "101", "111", "11"])

    Output: [15, 7, 3, 5, 1]
        (and after sortByBinaryOnes is: ["1111", "111", "11", "101", "1"]) """


# def key_funciton(num):
#     binary = format(num, 'b')
#     return -binary.count('1'), len(binary), num

# def sort_by_binary_ones(num_list):
#     return sorted(num_list, key=key_funciton)

# def sort_by_binary_ones(num_list):
#     return sorted(num_list, key=lambda x: (-bin(x).count('1'), x.bit_length(), x))

def sort_by_binary_ones(num_list):
    return sorted(num_list, key=lambda x: (-bin(x).count('1'), x))

q = sort_by_binary_ones([1, 3]), [3, 1]
q
q = sort_by_binary_ones([1, 2, 3, 4]), [3, 1, 2, 4]
q
q = sort_by_binary_ones([5, 2049, 3])
q
#      [3, 5, 2049]
q = sort_by_binary_ones([99, 51, 21, 7, 44, 50, 49, 25, 5, 80, 33, 1])
q
#      [51, 99, 7, 21, 25, 44, 49, 50, 5, 33, 80, 1]
q = sort_by_binary_ones([64911, 99135, 79470, 71603, 15771, 53995, 83834, 69245, 30172, 23484, 13547, 85480, 9915,
                         81484, 71921, 58818, 86245, 29602, 46785, 49497, 46660, 17511, 82710, 34018, 30852, 75843, 37394, 6928, 778, 16584])
q
#      [64911, 15771, 23484, 30172, 53995, 69245, 71603, 79470, 83834, 99135, 9915, 13547, 81484, 85480, 29602, 46785, 58818, 71921, 86245, 17511, 46660, 49497, 82710, 30852, 34018, 75843, 6928, 37394, 778, 16584]
