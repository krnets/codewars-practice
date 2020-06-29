""" 5kyu - RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result
in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here. """


# def rgb(r, g, b):
#     # r = r if r > 0 else 0
#     # g = g if g > 0 else 0
#     # b = b if b > 0 else 0

#     # r = r if r < 255 else 255
#     # g = g if g < 255 else 255
#     # b = b if b < 255 else 255

#     r = r if 0 <= r < 255 else 0 if r < 0 else 255
#     g = g if 0 <= g < 255 else 0 if g < 0 else 255
#     b = b if 0 <= b < 255 else 0 if b < 0 else 255

#     return ''.join(x[2:].zfill(2) for x in map(hex, [r, g, b])).upper()

# def rgb(r, g, b):
#     limits = lambda x: max(0, (min(255, x)))
#     return ''.join(x[2:].zfill(2) for x in map(hex, map(limits, [r, g, b]))).upper()

# def rgb(r, g, b):
#     clamp = lambda x: max(0, (min(255, x)))
#     return ''.join(f'{x:02x}' for x in map(clamp, [r, g, b])).upper()

# def rgb(r, g, b):
#     return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), [r, g, b]))

def rgb(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))


q = rgb(255, 255, 255), "FFFFFF"
q
q = rgb(255, 255, 300), "FFFFFF"
q
q = rgb(0, 0, 0),  "000000"
q
q = rgb(148, 0, 211), "9400D3"
q
q = rgb(0, 0, 0), "000000"
q
q = rgb(1, 2, 3), "010203"
q
q = rgb(255, 255, 255), "FFFFFF"
q
q = rgb(254, 253, 252), "FEFDFC"
q
q = rgb(-20, 275, 125), "00FF7D"
q
