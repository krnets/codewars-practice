// 7kyu - Ultimate Array Reverser

/* Given an array of strings, reverse them and their order in such way that their length stays the same as the length of the original inputs.

Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"} */

// function ultimateReverse(str) {
//     let res = []
//     let lenStrings = str.map(v => v.length)
//     let reversedStr = [...str.join('')].reverse().join('')
//     for (let i = 0, j = 0; j < str.length; j++) {
//         let len = lenStrings[j]
//         res.push(reversedStr.substr(i, len))
//         i += len
//     }
//     return res
// }

function ultimateReverse(str) {
    let arr = [...str.join('')].reverse()
    return str.map(v => arr.splice(0, v.length).join(''))
}

// function ultimateReverse(str) {
//     let arr = [...str.join('')]
//     return str.map(v => [...v].map(_ => arr.pop()).join(''))
// }

q = ultimateReverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"])
// ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]
q

q = ultimateReverse(["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"])
// ["How", "many", "shrimp", "do", "you", "have", "to", "eat","before", "your", "skin", "starts", "to", "turn", "pink?"]
q