def change(st):
    bits = ["0"] * 26
    offset = ord("a")

    for c in st.lower():
        if c.isalpha():
            bits[ord(c) - offset] = "1"

    return "".join(bits)
