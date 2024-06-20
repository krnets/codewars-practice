from collections import Counter, defaultdict

# def numericals(s):
#     freq, res = Counter(), ""
#     for c in s:
#         freq[c] += 1
#         res += str(freq[c])
#     return res


# def numericals(s):
#     freq, res = defaultdict(int), []
#     for c in s:
#         freq[c] = freq.get(c, 0) + 1
#         res.append(freq[c])
#     return "".join(map(str, res))


def numericals(s):
    freq, res = defaultdict(int), ""
    for c in s:
        freq[c] += 1
        res += str(freq[c])
    return res
