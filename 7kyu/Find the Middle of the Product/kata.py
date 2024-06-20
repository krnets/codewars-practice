def find_middle(st):
    if not st or not isinstance(st, str):
        return -1
    product = 1
    for c in st:
        if c.isdigit():
            product *= int(c)
    s_product = str(product)
    mid = (len(s_product) - 1) // 2
    return int(s_product[mid : -mid or len(s_product)])
