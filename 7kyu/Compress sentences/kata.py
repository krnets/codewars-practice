# def compress(sentence):
#     uniq_idx = dict()
#     counter = 0
#     res = ""

#     for word in sentence.lower().split():
#         if word not in uniq_idx:
#             uniq_idx[word] = str(counter)
#             counter += 1
#         res += uniq_idx[word]
#     return res


def compress(sentence):
    d = dict()
    return "".join(d.setdefault(s, str(len(d))) for s in sentence.lower().split())
