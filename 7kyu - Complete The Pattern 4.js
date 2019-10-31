// 7kyu - Complete The Pattern 4

function pattern(n) {
    for (var res = [], t = [], i = n; i > 0; i--) {
        t.push(i)
        t.sort((a, b) => a - b)
        res.push(t.join ``)
    }
    return res.reverse().join('\n')
}
// res.push(t.sort((a, b) => a - b).join``)

q = pattern(1) // "1"
q
q = pattern(2) // "12\n2"
q
q = pattern(5) // "12345\n2345\n345\n45\n5"
q
q = pattern(10)
q