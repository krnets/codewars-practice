// 7kyu - Complete The Pattern 3 (Horizontal Image of 2)

// function pattern(n) {
//     for (var res = [], i = n, t = []; i > 0; i--) {
//         t.push(i)
//         res.push(t.slice())
//     }
//     return res.map((v => v.join ``)).join('\n')
// }

function pattern(n) {
    for (var res = [], s = '', i = n; i > 0; i--)
        res.push(s += i)
    return res.join('\n')
}

q = pattern(1) // "1"
q
q = pattern(2) // "2\n21"
q
q = pattern(5) // "5\n54\n543\n5432\n54321"
q