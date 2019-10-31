// 8kyu - Double Char

// Given a string, you have to return a string in which each character (case-sensitive) is repeated once

// const doubleChar = str => [...str].map((c => c + c)).join``
const doubleChar = str => [...str].map((char => char.repeat(2))).join``

// const doubleChar = str => str.replace(/(.)/g, '$1$1')
// const doubleChar = str => str.replace(/./g, '$&$&')
// const doubleChar = str => str.replace(/./gi, (l) => l + l);

// function doubleChar(str) {
//     let newStr = ''
//     for (let i of str)
//         newStr += i.concat(i)
//     return newStr
// }

q = doubleChar("abcd") // "aabbccdd"
q
q = doubleChar("Adidas") //  "AAddiiddaass"
q
q = doubleChar("1337") // "11333377"
q
q = doubleChar("illuminati") // "iilllluummiinnaattii"
q
q = doubleChar("123456") // "112233445566"
q
q = doubleChar("%^&*(") // "%%^^&&**(("
q