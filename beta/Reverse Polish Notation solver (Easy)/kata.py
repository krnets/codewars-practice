def solve_postfix(pfx):
    stack = [0]
    for c in pfx.split():
        if c in "^*/+-":
            b = stack.pop()
            a = stack.pop()
            match c:
                case "+": stack.append(a + b)
                case "-": stack.append(a - b)
                case "*": stack.append(a * b)
                case "/": stack.append(a // b)
                case "^": stack.append(a**b)
        else:
            stack.append(int(c))
    return round(stack.pop())