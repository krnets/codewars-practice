""" 6kyu - Data Reverse

A stream of data is received and needs to be reversed.
Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)

should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)

The total number of bits will always be a multiple of 8.
The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0] """

# import re

# def data_reverse(data):
#     return [int(x) for byte in re.findall(r'\d{8}', ''.join(map(str, data)))[::-1] for x in byte]

# def data_reverse(data):
#     return data[-8:] + data_reverse(data[:-8]) if len(data) else []

# def data_reverse(data):
#     res = []
#     for i in range(len(data)-8, -1, -8):
#         res.extend(data[i:i+8])
#     return res


def data_reverse(data):
    return sum([data[i:i+8] for i in range(len(data), -1, -8)], [])


data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
q = data_reverse(data1)
q
#  [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
q = data_reverse(data3)
q
#  [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
