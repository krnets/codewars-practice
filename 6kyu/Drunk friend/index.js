// 6kyu - Drunk friend

// function decode(str) {
//     // let abc = 'abcdefghijklmnopqrstuvwxyz'
//     // let abcCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
//     let abcABC = 'abcdefghijklmnopqrstuvwxyz      ABCDEFGHIJKLMNOPQRSTUVWXYZ'
//     let a = str
//     a
//     let abcReversed = [...abcABC].reverse().join ``
//     abcReversed
//     let c = str.charCodeAt(0) - 65
//     c
//     let d = abcReversed[25]
//     d
//     let decoded = []
//     for (let i = 0; i < str.length; i++) {
//         if (/[A-Za-z]/.test(str[i])) {
//             decoded.push(abcReversed[str.charCodeAt(i) - 65])
//         } else {
//             decoded.push(str[i])
//         }
//     }
//     let e = str.charCodeAt(3)
//     e
//     return decoded.join``
// }

// function decode(str) {
//     let abcABC = 'abcdefghijklmnopqrstuvwxyz      ABCDEFGHIJKLMNOPQRSTUVWXYZ'
//     let abcReversed = [...abcABC].reverse().join ``
//     let decoded = []
//     for (let i = 0; i < str.length; i++) {
//         if (/[A-Za-z]/.test(str[i])) {
//             decoded.push(abcReversed[str.charCodeAt(i) - 65])
//         } else {
//             decoded.push(str[i])
//         }
//     }
//     return decoded.join ``
// }

// function decode(str) {
//     if (typeof str != 'string')
//         return 'Input is not a string'

//     let abcABC = 'abcdefghijklmnopqrstuvwxyz      ABCDEFGHIJKLMNOPQRSTUVWXYZ'
//     let abcReversed = [...abcABC].reverse().join ``
//     let decoded = []

//     for (let i = 0; i < str.length; i++) {
//         if (/[A-Za-z]/.test(str[i]))
//             decoded.push(abcReversed[str.charCodeAt(i) - 65])
//         else
//             decoded.push(str[i])
//     }
//     return decoded.join ``
// }

// const decode = str => typeof str == 'string' ? str.replace(/[A-Z]/g,
//     m => String.fromCharCode(155 - m.charCodeAt(0))).replace(/[a-z]/g,
//     m => String.fromCharCode(219 - m.charCodeAt(0))) : "Input is not a string"

// function decode(str) {
//     if (String(str) !== str)
//         return "Input is not a string";
//     str = str.replace(/[a-z]/g, a => String.fromCharCode(26 - (a.charCodeAt() - 96) + 97));
//     return str.replace(/[A-Z]/g, a => String.fromCharCode(26 - (a.charCodeAt() - 64) + 65));
// }

// const decode = str => (String(str) !== str) ? 'Input is not a string' :
//         str.replace(/[A-Z]/g, a => String.fromCharCode(26 - (a.charCodeAt() - 64) + 65))
//            .replace(/[a-z]/g, a => String.fromCharCode(26 - (a.charCodeAt() - 96) + 97))

const decode = str => (typeof str !== 'string') ? 'Input is not a string' :
    str.replace(/[a-zA-Z]/g, c => String.fromCharCode(((c = c.charCodeAt()) < 97 ? 155 : 219) - c))


q = decode("ABC abc 10") // "You already had 10 beers"
q
q = decode("yvvi") // "beer"
q
q = decode("Blf zoivzwb szw 10 yvvih") // "You already had 10 beers"
q
q = decode("Ovg'h hdrn rm gsv ulfmgzrm!") // "Let's swim in the fountain!"
q
q = decode("Tl slnv, blf'iv wifmp") // "Go home, you're drunk"
q