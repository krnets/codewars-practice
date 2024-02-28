def uglify_word(s):
    prev_is_upper = False
    res = ""

    for c in s:
        if c.isalpha():
            if prev_is_upper:
                res += c.lower()
            else:
                res += c.upper()
            prev_is_upper = not prev_is_upper
        else:
            res += c
            prev_is_upper = False

    return res
