# 8 kyu - Reversed Strings

""" Complete the solution so that it reverses the string value passed into it. """

# def solution(string):
#     return ''.join(reversed(string))

def solution(string):
    return string[::-1]

# def solution(string):
#     str = ""
#     for i in string:
#         str = i + string
#     return str

# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]


# def solution(string):
#     return reverse(string)

# def createStack():
#     stack = []
#     return stack


# def size(stack):
#     return len(stack)


# def isEmpty(stack):
#     return len(stack) == 0


# def push(stack, item):
#     stack.append(item)


# def pop(stack):
#     if isEmpty(stack):
#         return
#     return stack.pop()


# def reverse(string):
#     n = len(string)
#     stack = createStack()
#     for i in range(0, n, 1):
#         push(stack, string[i])
#     string = ""
#     for i in range(0, n, 1):
#         string += pop(stack)
#     return string


# def solution(string):
#     return reverse(string)


q = solution('world')  # returns 'dlrow'
q
q = solution('hello')  # 'olleh'
q
q = solution('')  # ''
q
q = solution('h')  # 'h'
q
