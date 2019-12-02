// 7kyu - Maximum Length Difference

/* You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. 
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 

a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13   */

function mxdiflg(s1, s2) {
    if (!s1.length || !s2.length) return -1
    let len1 = s1.map(v => v.length)
    let len2 = s2.map(v => v.length)
    return Math.max(Math.max(...len1) - Math.min(...len2), Math.max(...len2) - Math.min(...len1))
}

// function mxdiflg(s1, s2) {
//     let max = -1
//     for (let i of s1)
//         for (let j of s2)
//             max = Math.max(max, Math.abs(i.length - j.length))
//     return max
// }

var s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"];
var s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"];
q = mxdiflg(s1, s2) // 13
q