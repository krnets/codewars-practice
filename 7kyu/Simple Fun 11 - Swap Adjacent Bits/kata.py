def swap_adjacent_bits(n):
    bits = list(f"{n:032b}")

    for i in range(0, len(bits), 2):
        bits[i], bits[i + 1] = bits[i + 1], bits[i]

    return int("".join(bits), 2)
