from hashlib import sha1
from itertools import product
from string import ascii_lowercase

# def password_cracker(hash):
#     for n_chars in range(1, 6):
#         for combination in product(ascii_lowercase, repeat=n_chars):
#             pw_candidate = "".join(combination)
#             if sha1(pw_candidate.encode()).hexdigest() == hash:
#                 return pw_candidate


def password_cracker(hash):
    for n_chars in range(1, 6):
        for pw_candidate in map("".join, product(ascii_lowercase, repeat=n_chars)):
            if sha1(pw_candidate.encode()).hexdigest() == hash:
                return pw_candidate
