""" 6kyu - ASCII Cipher

We're going to create a cipher, so that we can send messages to our friends and no one else will know what cool things we're discussing. 

Our cipher will take two arguments: 
a key, in the form of an integer, and a message, in the form of a string.

Our first step is to find the largest prime of the key. 
For example, the prime factorization of 18 is 2 x 3 x 3, so the largest prime is 3. 
We'll also accept negative integers as keys, so -18 would give us a "largest" prime of -3. 
Once we've gotten our prime number, we'll encrypt our message.

The way we'll encrypt is to use the base ASCII table values of 0-127. 
We'll take the ASCII value of every character and add the value of our prime number. 
For example, the character 'D' has an ASCII value of 68, Adding 3 would give 71, which is 'G'.

So, this will look like the following:

If we're given a key of 18, and a message of "Hello, world", we'll calculate the largest prime to be 3, 
and then add it to the ASCII values of our string, giving an output of "Khoor/#zruog".

We'll let values greater than 127 or less than 0 "wrap around", and start at the other side of the ASCII table, 
so a -1 will be considered a 127, and a 128 will be considered a 0. """


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

def prime_factors(n):
    return [i for i in range(2, n+1) if n % i == 0 and is_prime(i)]

def ascii_cipher(message, key):
    sign = -1 if key < 0 else 1
    rot = max(prime_factors(abs(key))) * sign
    return ''.join(chr((ord(c) + rot) % 128) for c in message)

# def max_prime_factor(n):
#     k = n
#     for k in range(2, int(abs(n)**0.5)+1):
#         while n % k == 0:
#             n //= k
#         if n == 1:
#             return max(n, k)
#     return n


# def ascii_cipher(message, key):
#     rot = max_prime_factor(abs(key)) * (-1 if key < 0 else 1)
#     return ''.join(chr((ord(c) + rot) % 128) for c in message)


q = ascii_cipher("Hello, world", 18), "Khoor/#zruog"
q
q = ascii_cipher("Encryption rules!", 326), "hCD"
q
q = ascii_cipher("Imitation Game, up in here!", -
                 7), "BfbmZmbhg@Zf^%nibga^k^"
q
