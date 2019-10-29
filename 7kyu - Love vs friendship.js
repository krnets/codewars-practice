// 7kyu - Love vs friendship

// const wordsToMarks = string => [...string].map((v) => v.charCodeAt() - 96).reduce((a, b) => a + b)

// const wordsToMarks = string => [...string].reduce((a, b) => a + b.charCodeAt() - 96, 0)

const wordsToMarks = string => [...string].reduce((a, b) => a + " abcdefghijklmnopqrstuvwxyz".indexOf(b), 0)

// function wordsToMarks(string) {
//     let sum = 0
//     for (let char of string)
//         sum += char.charCodeAt() - 96
//     return sum
// }


q = wordsToMarks("attitude") //100
q
q = wordsToMarks("friends") // 75
q
q = wordsToMarks("family") // 66
q
q = wordsToMarks("selfness") // 99
q
q = wordsToMarks("knowledge") // 96
q