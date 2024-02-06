# def calc(expr):
#     stack = []
#     for t in expr.split():
#         match t:
#             case "+":
#                 y = stack.pop()
#                 x = stack.pop()
#                 stack.append(x + y)
#             case "-":
#                 y = stack.pop()
#                 x = stack.pop()
#                 stack.append(x - y)
#             case "*":
#                 y = stack.pop()
#                 x = stack.pop()
#                 stack.append(x * y)
#             case "/":
#                 y = stack.pop()
#                 x = stack.pop()
#                 stack.append(x / y)
#             case _:
#                 stack.append(float(t))

#     return stack.pop() if stack else 0


def calc(expr):
    stack = [0]
    for t in expr.split():
        if t in "+-*/":
            y = stack.pop()
            x = stack.pop()
            match t:
                case "+": stack.append(x + y)
                case "-": stack.append(x - y)
                case "*": stack.append(x * y)
                case "/": stack.append(x / y)
        else:
            stack.append(float(t))
    return stack.pop()
