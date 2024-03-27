def encode_resistor_colors(ohms_string):
    color_codes = {
        "0": "black",
        "1": "brown",
        "2": "red",
        "3": "orange",
        "4": "yellow",
        "5": "green",
        "6": "blue",
        "7": "violet",
        "8": "gray",
        "9": "white",
    }
    ohms = ohms_string.split()[0].replace("k", "*1e3").replace("M", "*1e6")
    a, b, *zeroes = str(int(eval(ohms)))
    return "{} {} {} gold".format(*map(color_codes.get, [a, b, str(len(zeroes))]))
