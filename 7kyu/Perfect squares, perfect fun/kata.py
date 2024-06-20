def square_it(digits):
    s_digits = str(digits)
    n = len(s_digits)
    sq_root = n**0.5
    if not sq_root.is_integer():
        return "Not a perfect square!"
    step = int(sq_root)
    return "\n".join(s_digits[i : i + step] for i in range(0, n, step))
