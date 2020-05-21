// 6kyu - Binary to Text (ASCII) Conversion

/* Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

Each 8 bits on the binary string represent 1 character on the ASCII table.
The input string will always be a valid binary string.
Characters can be in the range from "00000000" to "11111111" (inclusive)

Note: In the case of an empty binary string your function should return an empty string.
Fundamentals | Binary | ASCII | Character Encodings | Formats | Strings */

// function binaryToString(binary) {
//     for (var arr = [], i = 0; i < binary.length; i += 8)
//         arr.push(binary.substr(i, 8))
//     return arr.reduce((res, v) => res + String.fromCharCode(parseInt(v, 2)), '')
// }

function binaryToString(binary) {
    for (var str = '', i = 0; i < binary.length; i += 8)
        str += String.fromCharCode(parseInt(binary.substr(i, 8), 2))
    return str
}

// const binaryToString = (binary) => binary.replace(/[01]{8}/g, b => String.fromCharCode(parseInt(b, 2)))
// const binaryToString = (binary) => binary.replace(/.{8}/g, v => String.fromCharCode(`0b${v}`))


q = binaryToString('01100001') // 'a'
q
q = binaryToString('01001011010101000100100001011000010000100101100101000101') // 'KTHXBYE'
q
q = binaryToString('00110001001100000011000100110001') // '1011'
q
q = binaryToString('001111000011101000101001') // '<:)'
q