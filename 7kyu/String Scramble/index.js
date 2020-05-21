// 7kyu - String Scramble

// function scramble(str, arr) {
//     let newStr = ''
//     for (let i = 0; i < str.length; i++)
//         newStr += str[arr.indexOf(i)]
//     return newStr
// }

// function scramble(str, arr) {
//     for (var res = [], i = 0; i < str.length; i++)
//         res[arr[i]] = str[i]

//     return res.join ``
// }

const scramble = (str, arr) => arr.map((_, i) => str[arr.indexOf(i)]).join ``

// const scramble = (str, arr) => arr.reduce((acc, _, i) => acc + str[arr.indexOf(i)], '')


q = scramble('abcd', [0, 3, 1, 2]) // 'acdb'
q
q = scramble('sc301s', [4, 0, 3, 1, 5, 2]) // "c0s3s1"
q
q = scramble('bskl5', [2, 1, 4, 3, 0]) // "5sblk"
q

//  [2, 1, 4, 3, 0])
//  [0, 1, 2, 3, 4])