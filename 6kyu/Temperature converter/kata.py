def convert_temp(temp, from_scale, to_scale):
    match from_scale:
        case "C":  in_celsius = temp
        case "F":  in_celsius = (temp - 32) * 5 / 9
        case "K":  in_celsius = temp - 273.15
        case "R":  in_celsius = (temp - 491.67) * 5 / 9
        case "De": in_celsius = 100 - temp * 2 / 3
        case "N":  in_celsius = temp * 100 / 33
        case "Re": in_celsius = temp * 5 / 4
        case "Ro": in_celsius = (temp - 7.5) * 40 / 21
        case _:    in_celsius = 0

    match to_scale:
        case "C":  return in_celsius
        case "F":  return int(in_celsius * 9 / 5 + 32)
        case "K":  return int(in_celsius + 273.15)
        case "R":  return int((in_celsius + 273.15) * 5 / 9)
        case "De": return int((100 - in_celsius) * 3 / 2)
        case "N":  return int(in_celsius * 33 / 100)
        case "Re": return int(in_celsius * 4 / 5)
        case "Ro": return int(in_celsius * 21 / 40 + 7.5)
        case _:    return 0
