def sticky_calc(operation, val1, val2):
    val2 = round(val2)
    val1 = int("{}{}".format(round(val1), val2))
    match operation:
        case "+": return val1 + val2
        case "-": return val1 - val2
        case "*": return round(val1 * val2)
        case "/": return round(val1 / val2)
