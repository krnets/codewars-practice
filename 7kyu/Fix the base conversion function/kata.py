def convert_num(number, base):
    if isinstance(number, int):
        match base:
            case "hex": return hex(number)
            case "bin": return bin(number)
            case _:     return "Invalid base input"
    return "Invalid number input"
