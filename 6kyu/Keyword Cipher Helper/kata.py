# class keyword_cipher(object):
#     def __init__(self, abc, keyword):
#         self.clean_keyword = self.get_unique_chars(keyword)
#         self.cipher = self.clean_keyword + "".join(sorted(set(abc).difference(keyword)))
#         self.encode_trans_table = str.maketrans(abc, self.cipher)
#         self.decode_trans_table = str.maketrans(self.cipher, abc)

#     def encode(self, plain):
#         return plain.translate(self.encode_trans_table)

#     def decode(self, ciphered):
#         return ciphered.translate(self.decode_trans_table)

#     def get_unique_chars(self, keyword):
#         seen, uniq = set(), []
#         for c in keyword:
#             if c not in seen:
#                 uniq.append(c)
#                 seen.add(c)
#         return "".join(uniq)


class keyword_cipher(object):
    def __init__(self, abc, keyword):
        #     self.keyword_deduped = "".join(sorted(ks := set(keyword), key=keyword.index))
        #     self.cipher_key = self.keyword_deduped + "".join(sorted(set(abc).difference(ks)))
        self.cipher_key = "".join(dict.fromkeys(keyword + abc).keys())
        self.encode_trans_table = str.maketrans(abc, self.cipher_key)
        self.decode_trans_table = str.maketrans(self.cipher_key, abc)

    def encode(self, plain):
        return plain.translate(self.encode_trans_table)

    def decode(self, ciphered):
        return ciphered.translate(self.decode_trans_table)
