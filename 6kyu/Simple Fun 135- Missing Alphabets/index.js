// 6kyu - Simple Fun #135: Missing Alphabets

/* Given string s, which contains only letters from a to z in lowercase.

A set of alphabet is given by abcdefghijklmnopqrstuvwxyz.
2 sets of alphabets mean 2 or more alphabets.

Your task is to find the missing letter(s). You may need to output them by the order a-z. 
It is possible that there is more than one missing letter from more than one set of alphabet.

If the string contains all of the letters in the alphabet, return an empty string ""

For s='abcdefghijklmnopqrstuvwxy'
The result should be 'z'

For s='aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy'
The result should be 'zz'

For s='abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy'
The result should be 'ayzz'

For s='codewars'
The result should be 'bfghijklmnpqtuvxyz'

    [input] string s
    Given string(s) contains one or more set of alphabets in lowercase.

    [output] a string
    Find the letters contained in each alphabet but not in the string(s). Output them by the order a-z. 
    If missing alphabet is repeated, please repeat them like "bbccdd", not "bcdbcd" */

// function missingAlphabets(s) {
//     let diff = {}
//     let abc = [...'a'.repeat(26)].map((c, i) => String.fromCharCode(c.charCodeAt() + i))
//     let freqA = [...s].reduce((count, v) => (count[v] = ++count[v] || 1, count), {})
//     let vals = Object.values(freqA)
//     let avg = Math.round(vals.reduce((a, b) => a + b, 0) / vals.length)
//     let freqB = [...abc.map(v => v.repeat(avg)).join('')].reduce((count, v) => (count[v] = ++count[v] || 1, count), {})
//     for (let key in freqB) {
//         if (freqA.hasOwnProperty(key))
//             diff[key] = freqB[key] - freqA[key]
//         else
//             diff[key] = freqB[key]
//     }
//     return Object.entries(diff).filter(v => v[1] > 0).map(v => v[0].repeat(v[1])).join('')
// }


// function missingAlphabets(s) {
//     let diff = {}
//     let abc = [...'a'.repeat(26)].map((c, i) => String.fromCharCode(c.charCodeAt() + i))
//     let freqA = [...s].reduce((count, v) => (count[v] = ++count[v] || 1, count), {})
//     let vals = Object.values(freqA)
//     let avg = Math.round(vals.reduce((a, b) => a + b, 0) / vals.length)
//     let freqB = [...abc.map(v => v.repeat(avg)).join('')].reduce((count, v) => (count[v] = ++count[v] || 1, count), {})
//     for (let key in freqB) {
//         if (freqA.hasOwnProperty(key))
//             diff[key] = freqB[key] - freqA[key]
//         else
//             diff[key] = freqB[key]
//     }
//     return Object.entries(diff).filter(v => v[1] > 0).map(v => v[0].repeat(v[1])).join('')
// }

// function missingAlphabets(s) {
//     let abc = [...'a'.repeat(26)].map((c, i) => String.fromCharCode(c.charCodeAt() + i)).join('')
//     let freqA = [...s].reduce((count, v) => (count[v] = ++count[v] || 1, count), {})
//     let max = Math.max(...Object.values(freqA))
//     let mult = abc.replace(/./g, v => v.repeat(max))
//     let freqB = [...mult].reduce((count, v) => (count[v] = ++count[v] || 1, count), {})
//     let res = []
//     for (let c in freqB) {
//         if (freqA[c]) {
//             if (freqB[c] - freqA[c] > 0)
//                 res.push(c.repeat(freqB[c] - freqA[c]))
//         } else {
//             res.push(c.repeat(freqB[c]))
//         }
//     }
//     return res.join('')
// }

// function missingAlphabets(s) {
//     const counts = new Map(Array.from("abcdefghijklmnopqrstuvwxyz", c => [c, 0]))
//     for (const c of s) counts.set(c, counts.get(c) + 1)
//     const alphabets = Math.max(...counts.values())
//     return [...counts].reduce((xs, [c, n]) => xs + c.repeat(alphabets - n), "")
// }

function missingAlphabets(s) {
    let freq = [...s].reduce((count, v) => (count[v] = ++count[v] || 1, count), {})
    let max = Math.max(...Object.values(freq))
    return [...'abcdefghijklmnopqrstuvwxyz'].map(v => v.repeat(max - (freq[v] || 0))).join('')
}

q = missingAlphabets("abcdefghijklmnopqrstuvwxy") // "z"
q
q = missingAlphabets("abcdefghijklmnopqrstuvwxyz") // ""
q
q = missingAlphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy") // "zz"
q
q = missingAlphabets("abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy") // "ayzz"
q
q = missingAlphabets("codewars") // "bfghijklmnpqtuvxyz"
q