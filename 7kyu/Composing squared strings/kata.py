def compose(s1, s2):
    t1 = [x[:i] for i, x in enumerate(s1.split("\n"), 1)]
    t2 = [y[:i] for i, y in enumerate(s2.split("\n"), 1)]
    return "\n".join(x + y for x, y in zip(t1, reversed(t2)))


# s1 = "abcd\nefgh\nijkl\nmnop"
# s2 = "qrst\nuvwx\nyz12\n3456"

# abcd
# efgh
# ijkl
# mnop"

# qrst
# uvwx
# yz12
# 3456"

# a3456\nefyz1\nijkuv\nmnopq

# abcd    qrst  -->  a3456
# efgh    uvwx       efyz1
# ijkl    yz12       ijkuv
# mnop    3456       mnopq
