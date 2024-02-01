# def valid_braces(string):
#     stack = []
#     matching_braces = {")": "(", "]": "[", "}": "{"}

#     for c in string:
#         if c in matching_braces:
#             if not stack or matching_braces[c] != stack[-1]:
#                 return False
#             else:
#                 stack.pop()
#         else:
#             stack.append(c)

#     return not stack


def valid_braces(string):
    stack = []
    matching_braces = {"(": ")", "[": "]", "{": "}"}

    for c in string:
        if c in matching_braces:
            stack.append(c)
        else:
            if not stack or matching_braces[stack[-1]] != c:
                return False
            else:
                stack.pop()

    return not stack
