from collections import defaultdict, deque


# def substring(strng):
#     longest, current = deque(), deque()
#     char_counter = defaultdict(int)

#     for c in strng:
#         current.append(c)
#         char_counter[c] += 1

#         while len(char_counter) > 2:
#             d = current.popleft()
#             char_counter[d] -= 1
#             if char_counter[d] == 0:
#                 del char_counter[d]

#         if len(longest) < len(current):
#             longest = current.copy()

#     return "".join(longest)

import re


# def substring(strng):
#     if len(strng) <= 2:
#         return strng
#     pattern = r"((.)\2*)(?=((.)\4*(?:\2|\4)*))"
#     return max((x + y for x, _, y, _ in re.findall(pattern, strng)), key=len, default="")


def substring(strng):
    if len(set(strng)) <= 2:
        return strng
    pattern = re.compile(r"(.)\1*(.)(\1|\2)*")
    return max((pattern.search(strng, i).group() for i in range(len(strng) - 1)), key=len)
