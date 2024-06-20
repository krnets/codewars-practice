def tap_code_translation(text):
    table = ["ABCDE", "FGHIJ", "LMNOP", "QRSTU", "VWXYZ"]
    codes = {c: (i, j) for i, row in enumerate(table, 1) for j, c in enumerate(row, 1)}
    codes["K"] = codes["C"]
    res = []

    for c in text.upper():
        i, j = codes.get(c, (0, 0))
        res.append("." * i)
        res.append("." * j)

    return " ".join(res)
