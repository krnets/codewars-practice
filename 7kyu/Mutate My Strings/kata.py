def mutate_my_strings(s1, s2):
    res = [s1]
    chars = list(s1)

    for i, c in enumerate(s2):
        if chars[i] != c:
            chars[i] = c
            res.append("".join(chars))

    return "\n".join(res) + "\n"
