// 7kyu - Unique string characters

/* In this Kata, you will be given two strings a and b and your task will be to return the characters that are 
not common in the two strings.

solve("xyab","xzca") = "ybzc" 

--The first string has 'yb' which is not in the second string. 
--The second string has 'zc' which is not in the first string. 

Notice also that you return the characters from the first string concatenated with those from the second string. */

// function solve(a, b) {
//     let aa = [...a].filter(v => !b.includes(v))
//     let bb = [...b].filter(v => !a.includes(v))
//     return aa.concat(bb).join('')
// }

// const solve = (a, b) => [].concat([...a].filter(v => !b.includes(v)), [...b].filter(v => !a.includes(v))).join('')

const solve = (a, b) => [...(a + b)].filter(ch => a.includes(ch) ^ b.includes(ch)).join('')

// function solve(a, b) {
//     let setA = new Set(a)
//     let setB = new Set(b)
//     return [...a + b].filter(c => setA.has(c) ^ setB.has(c)).join('')
// }

q = solve("xyab", "xzca") // "ybzc"
q
q = solve("xyabb", "xzca") // "ybbzc"
q
q = solve("abcd", "xyz") // "abcdxyz"
q
q = solve("xxx", "xzca") // "zca"
q