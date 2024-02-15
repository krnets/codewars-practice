def shorten(string, length, glue="..."):
    n_str = len(string)
    n_glue = len(glue)

    if length > n_str or n_glue + 2 > n_str or n_glue + 2 > length:
        return string[:length]

    n_left = (length - n_glue) // 2
    n_right = length - n_glue - n_left

    return string[:n_left] + glue + string[-n_right:]
