def my_first_interpreter(code):
    ans, pos = "", 0
    for c in code:
        match c:
            case ".": ans += chr(pos)
            case "+": pos = (pos + 1) % 256
    return ans
