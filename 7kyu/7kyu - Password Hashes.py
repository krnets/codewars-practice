# 7kyu - Password Hashes

""" When you sign up for an account somewhere, some websites do not actually store your password 
in their databases. Instead, they will transform your password into something else using a 
cryptographic hashing algorithm.

After the password is transformed, it is then called a password hash. Whenever you try to login, 
the website will transform the password you tried using the same hashing algorithm and simply see 
if the password hashes are the same.

Create the function that converts a given string into an md5 hash. The return value should be encoded 
in hexadecimal.

passHash("password") // --> "5f4dcc3b5aa765d61d8327deb882cf99"
passHash("abc123") // --> "e99a18c428cb38d5f260853678922e03"

If you want to externally test a string, look at this website.

As a side note, md5 can be exploited, so never use it for anything secure. The reason I used it in 
this kata is simply because it is a very common hashing algorithm and many people will recognize the name. """

# import math

# rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
#                   5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
#                   4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
#                   6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

# constants = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

# init_values = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

# functions = 16*[lambda b, c, d: (b & c) | (~b & d)] + \
#             16*[lambda b, c, d: (d & b) | (~d & c)] + \
#             16*[lambda b, c, d: b ^ c ^ d] + \
#             16*[lambda b, c, d: c ^ (b | ~d)]

# index_functions = 16*[lambda i: i] + \
#                   16*[lambda i: (5*i + 1)%16] + \
#                   16*[lambda i: (3*i + 5)%16] + \
#                   16*[lambda i: (7*i)%16]

# def left_rotate(x, amount):
#     x &= 0xFFFFFFFF
#     return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF

# def md5(message):
#     message = bytearray(message, encoding='ascii') #copy our input into a mutable buffer
#     orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
#     message.append(0x80)
#     while len(message)%64 != 56:
#         message.append(0)
#     message += orig_len_in_bits.to_bytes(8, byteorder='little')

#     hash_pieces = init_values[:]

#     for chunk_ofst in range(0, len(message), 64):
#         a, b, c, d = hash_pieces
#         chunk = message[chunk_ofst:chunk_ofst+64]
#         for i in range(64):
#             f = functions[i](b, c, d)
#             g = index_functions[i](i)
#             to_rotate = a + f + constants[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
#             new_b = (b + left_rotate(to_rotate, rotate_amounts[i])) & 0xFFFFFFFF
#             a, b, c, d = d, new_b, b, c
#         for i, val in enumerate([a, b, c, d]):
#             hash_pieces[i] += val
#             hash_pieces[i] &= 0xFFFFFFFF

#     return sum(x<<(32*i) for i, x in enumerate(hash_pieces))


# def pass_hash(str):
#     digest = md5(str)
#     raw = digest.to_bytes(16, byteorder='little')
#     return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))


import hashlib

def pass_hash(str):
    return hashlib.md5(str.encode()).hexdigest()


q = pass_hash('password')  # '5f4dcc3b5aa765d61d8327deb882cf99'
q
q = pass_hash('abc123')  # 'e99a18c428cb38d5f260853678922e03'
q
