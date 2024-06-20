def center(strng, width, fill=" "):
    n = len(strng)
    return fill * ((width - n + 1) // 2) + strng + fill * ((width - n) // 2)
