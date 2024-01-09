def valid_parentheses(paren_str):
    stack = []

    for paren in paren_str:
        if paren == ")":
            if not stack or stack[-1] == paren:
                return False
            else:
                stack.pop()
        else:
            stack.append(paren)

    return not stack
