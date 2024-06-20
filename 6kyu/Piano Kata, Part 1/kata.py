# def black_or_white_key(key_press_count):
#     layout88 = "010" + ("01010" + "0101010") * 7 + "0"
#     return ("white", "black")[layout88[(key_press_count - 1) % 88] == "1"]


def black_or_white_key(key_press_count):
    piano_hex = "0x4" + "a54" * 7
    piano_binary = bin(int(piano_hex, 16)).replace("b", "")
    return ("white", "black")[piano_binary[(key_press_count - 1) % 88] == "1"]
