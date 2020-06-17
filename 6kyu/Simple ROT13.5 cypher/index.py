""" 6kyu - Simple ROT13.5 cypher

You are asked to write a simple cypher that rotates every character 
(in range [a-zA-Z], special chars will be ignored by the cipher) by 13 chars. 
As an addition to the original ROT13 cipher, this cypher will also cypher numerical digits ([0-9]) with 5 chars.

"The quick brown fox jumps over the 2 lazy dogs" -> 
"Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf"

Your task is to write a ROT13.5 (ROT135) method that accepts a string and encrypts it. 
Decrypting is performed by using the same method, but by passing the encrypted string again.

Note: when an empty string is passed, the result is also empty.
When passing your succesful algorithm, some random tests will also be applied.  """

# from string import ascii_lowercase as abc


# def ROT135(input):
#     res = []
#     for x in input:
#         if x.isdigit():
#             res.append(str((int(x) + 5) % 10))
#         elif x.isupper():
#             res.append(abc[(abc.index(x.lower()) + 13) % 26].upper())
#         elif x.isalpha():
#             res.append(abc[(abc.index(x) + 13) % 26])
#         else:
#             res.append(x)
#     return ''.join(res)

from string import digits as d, ascii_uppercase as ABC, ascii_lowercase as abc

def ROT135(input):
    cypher = dict(list(zip(d, (d+d)[5:])) +
                  list(zip(ABC, (ABC + ABC)[13:])) +
                  list(zip(abc, (abc + abc)[13:])))
    return ''.join(cypher.get(x, x) for x in input)


# def ROT135(input):
#     return input.translate(str.maketrans(d+ABC+abc,  d[5:] + d[:5] + ABC[13:] + ABC[:13] + abc[13:] + abc[:13]))

# from codecs import encode

# def ROT135(input):
#     return encode(input, 'rot13').translate(str.maketrans(d, d[5:]+d[:5]))


q = ROT135("The quick brown fox jumps over the 2 lazy dogs")
q
#     "Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf"

q = ROT135("Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf")
q
#     "The quick brown fox jumps over the 2 lazy dogs"
