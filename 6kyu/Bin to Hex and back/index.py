""" 6kyu - Bin to Hex and back

Define two functions: hex_to_bin and bin_to_hex (or hexToBin and binToHex)
hex_to_bin

Takes a hexadecimal string as an argument .

Note: This string can contain upper or lower case characters and start with any amount of zeros.

Returns the binary representation (without leading zeros) of the numerical value of the hexadecimal string.

Examples:

"00F"    -->  "1111"
"5"      -->  "101"
"00000"  -->  "0"
"04D2"   -->  "10011010010"

bin_to_hex

Takes a binary string (with or without leading zeros) as an argument .

Returns the hexadecimal representation of the numerical value of the binary string.

Note: Any non-numerical characters should be lower case

Examples:

"1111"         -->  "f"
"000101"       -->  "5"
"10011010010"  -->  "4d2"

Note: You can assume all arguments are valid so there is no need for error checking.

built-in functions bin, hex and int are disabled """


# HEX_BIN = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
#            '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#            'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# BIN_HEX = {v: k for k, v in HEX_BIN.items()}


# def cleanup_fmt(string):
#     if all(x == '0' for x in string):
#         return '0'
#     for i in range(len(string)):
#         if string[i] != '0':
#             return string[i:].lower()

# def bin_to_hex(binary_string):
#     bin_str = binary_string.rjust(64, '0')
#     res = ''.join(BIN_HEX[bin_str[i:i+4]] for i in range(0, 64, 4))
#     return cleanup_fmt(res)

# def hex_to_bin(hex_string):
#     res = ''.join([HEX_BIN[x] for x in hex_string.upper()])
#     return cleanup_fmt(res)


# def bin_to_hex(binary_string):
#     bin_str = binary_string.rjust(64, '0')
#     res = ''.join(BIN_HEX[bin_str[i:i+4]] for i in range(0, 64, 4))
#     return res.lstrip('0').lower() or '0'


# def hex_to_bin(hex_string):
#     res = ''.join([HEX_BIN[x] for x in hex_string.upper()])
#     return res.lstrip('0') or '0'


def bin_to_hex(binary_string):
    n = sum(2**i for i, b in enumerate(binary_string[::-1]) if b == '1')
    return f'{n:x}'


def hex_to_bin(hex_string):
    n = sum('0123456789ABCDEF'.index(x) * 16**i for i, x
            in enumerate(reversed(hex_string.upper())))
    return f'{n:b}'


q = hex_to_bin(
    '24ba2590effa7'), '10010010111010001001011001000011101111111110100111'
q
q = hex_to_bin('0'), '0'
q
q = hex_to_bin('f'), '1111'
q
q = hex_to_bin('0F'), '1111'
q
q = hex_to_bin('5'), '101'
q
q = hex_to_bin('04D2'), '10011010010'
q

q = bin_to_hex(
    '10010010111010001001011001000011101111111110100111'), '24ba2590effa7'
q
q = bin_to_hex('001111'), 'f'
q
q = bin_to_hex('000'), '0'
q
q = bin_to_hex('10011010010'), '4d2'
q
q = bin_to_hex(
    '1100000100001101111111101101001000101001100010010'), '1821bfda45312'
q
