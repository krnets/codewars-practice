// 6kyu - Break camelCase

// Complete the solution so that the function will break up camel casing, using a space between words.

// function solution(string) {
//     let res = ''
//     for (let i = 0; i < string.length; i++) {
//         if (string[i].toUpperCase() == string[i]) {
//             res += ' '
//             res += string[i]
//         } else
//             res += string[i]
//     }
//     return res
// }

const solution = string => [...string].map(v => v.toUpperCase() == v ? ' ' + v : v).join ``

// const solution = string => string.replace(/([A-Z])/g, ' $1')

q = solution('camelCasing') // 'camel Casing'
q