def calculator(txt):
    a, op, b = txt.split()
    res = '.'
    match op:
        case '+': res *= (len(a) + len(b)) 
        case '-': res *= (len(a) - len(b)) 
        case '*': res *= (len(a) * len(b)) 
        case '//': res *= (len(a) // len(b))
        case _: res  = ''
    return res
