// 7kyu - Reversing Fun

// function flipNumber(n) {
//     let res = []
//     let digits = [...n]
//     let len = digits.length
//     for (let i = 0; i < len; i++)
//         res.push(digits.reverse().splice(0, 1))
//     return res.reduce((a, b) => a.concat(b)).join ``
// }

// function flipNumber(n) {
//     let res = []
//     let digits = [...n]
//     while (digits.length)
//         res.push(digits.reverse().shift())
//     return res.join ``
// }

const flipNumber = n => n.length < 2 ? n : n.slice(-1) + n[0] + flipNumber(n.slice(1, -1))

q = flipNumber("012") // "201"
q
q = flipNumber("012345") // "504132"
q
q = flipNumber("0123456789") // "9081726354"
q