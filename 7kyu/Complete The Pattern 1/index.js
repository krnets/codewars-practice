// 7kyu - Complete The Pattern 1

// const pattern = n => Array.from({ length: n }, (_,i) => i + 1)
// const pattern = n => Array.from({ length: n }, (_,i) => i + 1).map((v,i,a) => String(v).repeat(v))
// const pattern = n => Array.from({ length: n }, (_, i) => i + 1).map((v, i, a) => String(v).repeat(v)).join('\n')
const pattern = n => Array.from({ length: n }, (_, i) => (String(i + 1).repeat(i + 1))).join('\n')

// function pattern(n) {
//     for (var res = [], i = 0; i < n; i++)
//         res.push((String(i + 1)).repeat(i + 1))
//     return res.join('\n')
// }

// function pattern(n) {
//     for (var res = [], i = 0; i <= n; i++)
//         res.push((Array(i + 1)).join(i))
//     return res.join('\n')
// }

q = pattern(1) // "1"
q
q = pattern(2) // "1\n22"
q
q = pattern(5) // "1\n22\n333\n4444\n55555"
q