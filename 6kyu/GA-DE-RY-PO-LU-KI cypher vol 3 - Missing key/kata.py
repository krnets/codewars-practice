from collections import defaultdict


# def find_the_key(messages, secrets):
#     d = defaultdict(str)

#     for m, s in zip("".join(messages), "".join(secrets)):
#         if m != s:
#             d[m] = s
#             d[s] = m

#     return "".join(sorted(set(k + v if k < v else v + k for k, v in d.items())))

# for m, s in zip("".join(messages), "".join(secrets)):
#     if m != s:
#         pairs.add(m + s if m < s else s + m)


# def find_the_key(messages, secrets):
#     pairs = {
#         m + s if m < s else s + m
#         for m, s in zip("".join(messages), "".join(secrets))
#         if m != s
#     }

#     return "".join(sorted(pairs))


def find_the_key(messages, secrets):
    return "".join(sorted({
                min(m, s) + max(m, s)
                for m, s in zip("".join(messages), "".join(secrets))
                if m != s }))
