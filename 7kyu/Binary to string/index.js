// 7kyu - Binary to string

// const binaryToString = binary => binary.split(/0b/).map(v => String.fromCharCode(parseInt(v, 2))).join``.slice(1)
const binaryToString = binary => String.fromCharCode(...binary.split( /(?=0b)/ ).map(Number))

q = binaryToString('0b10000110b11000010b1110100')
q
// 'Cat'
q = binaryToString('0b10010000b11001010b11011000b11011000b11011110b1000000b10101110b11011110b11100100b11011000b11001000b100001')
q
// 'Hello World!'
q = binaryToString('0b10100110b11001010b11000110b11100100b11001010b11101000b1000000b11011010b11001010b11100110b11100110b11000010b11001110b11001010b1000000b110001')
q
// 'Secret message 1'