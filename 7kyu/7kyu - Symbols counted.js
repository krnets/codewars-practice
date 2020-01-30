// 7kyu - Symbols counted 

/* In this kata you will have to transform each string so that it contains count for every symbol it contains, 
starting from 2. The order of symbols should be preserved.

Example: abbreviation => a2b2revi2ton */

// function transform(s) {
//     let res = ''
//     let countAbc = {};
//     [...s].forEach(v => countAbc[v] = ++countAbc[v] || 1)
//     for (let i = 0; i < s.length; i++) {
//         if (countAbc[s[i]] == 1)
//             res += s[i]
//         if (!res.includes(s[i])) {
//             res += s[i]
//             res += countAbc[s[i]]
//         }
//     }
//     return res
// }

// function transform(str) {
//     let countABC = new Map()
//     for (let char of str)
//         countABC.set(char, (countABC.get(char) || 0) + 1)
//     return Array.from(countABC, ([char, n]) => n == 1 ? char : char + n).join('')
// }

// function transform(str) {
//     let counts = {}
//     for (let c of str)
//         counts[c] = counts[c] + 1 || 1
//     return Object.entries(counts).map(v => v.join('')).join('').replace(/1/g, '')
// }

function transform(str) {
    let count = [...str].reduce((r, v) => (r[v] = ++r[v] || 1, r), {})
    return Object.keys(count).map(v => count[v] == 1 ? v : v + count[v]).join('')
}

q = transform('elevation') // 'e2lvation'
q
q = transform('transplantology') // 't2ra2n2spl2o2gy'
q
q = transform('economics') // 'ec2o2nmis'
q
q = transform('embarrassed') // 'e2mba2r2s2d'
q
q = transform('impressive') // 'i2mpre2s2v'
q