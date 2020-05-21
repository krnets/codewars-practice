// 6kyu - Base Conversion

/* In this kata you have to implement a base converter, which converts positive integers between arbitrary bases / pre-defined alphabets. 

The function convert() should take an input (string), the source alphabet (string) and the target alphabet (string). 
You can assume that the input value always consists of characters from the source alphabet. You don't need to validate it.

    The maximum input value can always be encoded in a number without loss of precision in JavaScript. 
    The function must work for any arbitrary alphabets, not only the pre-defined ones
    You don't have to consider negative numbers */

var Alphabet = {
    BINARY: '01',
    OCTAL: '01234567',
    DECIMAL: '0123456789',
    HEXA_DECIMAL: '0123456789abcdef',
    ALPHA_LOWER: 'abcdefghijklmnopqrstuvwxyz',
    ALPHA_UPPER: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    ALPHA: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    ALPHA_NUMERIC: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
};
var bin = Alphabet.BINARY,
    oct = Alphabet.OCTAL,
    dec = Alphabet.DECIMAL,
    hex = Alphabet.HEXA_DECIMAL,
    allow = Alphabet.ALPHA_LOWER,
    alup = Alphabet.ALPHA_UPPER,
    alpha = Alphabet.ALPHA,
    alnum = Alphabet.ALPHA_NUMERIC;


function convert(input, source, target) {
    let num = 0
    let str = ''
    for (let i = 0; i < input.length; i++) {
        num = num * source.length + source.indexOf(input[i])
    }
    while (num > 0) {
        str = target[num % target.length] + str
        num = Math.floor(num / target.length)
    }
    return str ? str : target[0]
}

// it('should convert between numeral systems', function() {
q = convert("15", dec, bin) // '1111', '"15" dec -> bin'
q
q = convert("15", dec, oct) // '17', '"15" dec -> oct'
q
q = convert("1010", bin, dec) // '10', '"1010" bin -> dec'
q
q = convert("1010", bin, hex) // 'a', '"1010" bin -> hex'
q
// // it('should convert between other bases', function() {
q = convert("0", dec, alpha) // 'a', '"0" dec -> alpha'
q
q = convert("27", dec, allow) // 'bb', '"27" dec -> alpha_lower'
q
q = convert("hello", allow, hex) // '320048', '"hello" alpha_lower -> hex
q
q = convert("SAME", alup, alup) // 'SAME', '"SAME" alpha_upper -> alpha_upper'
q