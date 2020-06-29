""" 5kyu - Convert A Hex String To RGB

When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) 
component values for a color. Implement a function that meets these requirements:

    Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
    Returns an object with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255

Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF") """


# def hex_string_to_RGB(hex_string):
#     rgb = 'rgb'
#     vals = [int(hex_string[i:i+2], 16) for i in range(1, len(hex_string), 2)]
#     return dict((rgb[i], vals[i]) for i in range(len(rgb)))

# def hex_string_to_RGB(hex_string):
#     return {'rgb'[i]: int(hex_string[i*2+1:i*2+3], 16) for i in range(3)}

# def hex_string_to_RGB(hex_string):
#     return {c: int(hex_string[1+2*i:3+2*i], 16) for i, c in enumerate('rgb')}

def hex_string_to_RGB(hex_string):
    return {c: int(hex_string[i:i+2], 16) for c, i in zip('rgb', [1, 3, 5])}

# def hex_string_to_RGB(hex_string):
#     hex_val = int(hex_string[1:], 16)
#     mask = 0x00ff
#     return {'r': hex_val >> 16 & mask, 'g': hex_val >> 8 & mask, 'b': hex_val & mask}


q = hex_string_to_RGB("#FF9933"), {'r': 255, 'g': 153, 'b': 51}
q
q = hex_string_to_RGB("#beaded"), {'r': 190, 'g': 173, 'b': 237}
q
q = hex_string_to_RGB("#000000"), {'r': 0, 'g': 0, 'b': 0}
q
q = hex_string_to_RGB("#111111"), {'r': 17, 'g': 17, 'b': 17}
q
q = hex_string_to_RGB("#Fa3456"), {'r': 250, 'g': 52, 'b': 86}
q
