# enc_key = "PLAYFIREXMBCDGHKNOQSTUVWZ"
from string import ascii_uppercase as ABC


def encipher(s, key):
    spaces_idx = []

    for i, c in enumerate(s):
        if c == " ":
            spaces_idx.append(i)

    s = s.upper().replace("J", "I")
    joined = s.replace(" ", "")
    joined_with_x = [joined[0]]

    for c in joined[1:]:
        if joined_with_x[-1] == c:
            joined_with_x.append("X")
        joined_with_x.append(c)

    if len(joined_with_x) & 1:
        joined_with_x.append("X")

    pairs = [(x, y) for x, y in zip(joined_with_x[::2], joined_with_x[1::2])]
    out_pairs_joined = ""
    key = key.upper().replace(" ", "")
    interim_keys = dict.fromkeys(key)

    for c in ABC:
        if c not in interim_keys:
            interim_keys[c] = None

    interim_keys.pop("J")
    enc_key = "".join(interim_keys.keys())
    enc_table = [enc_key[i : i + 5] for i in range(0, 25, 5)]
    enc_table_transposed = ["".join(tup) for tup in zip(*enc_table)]

    for x, y in pairs:
        translated = ""

        for row in enc_table:
            xi = row.find(x)
            yi = row.find(y)
            if xi >= 0 and yi >= 0:
                translated = row[(xi + 1) % 5] + row[(yi + 1) % 5]
                break

        if translated == "":
            for row in enc_table_transposed:
                xi = row.find(x)
                yi = row.find(y)
                if xi >= 0 and yi >= 0:
                    translated = row[(xi + 1) % 5] + row[(yi + 1) % 5]
                    break

        if translated == "":
            xi, xj = 0, 0
            yi, yj = 0, 0
            for i, row in enumerate(enc_table):
                for j, val in enumerate(row):
                    if x == val:
                        xi, xj = i, j
                    if y == val:
                        yi, yj = i, j
            translated = enc_table[xi][yj] + enc_table[yi][xj]

        out_pairs_joined += translated

    res = list(out_pairs_joined)

    for i in spaces_idx:
        res.insert(i, " ")

    return "".join(res)
