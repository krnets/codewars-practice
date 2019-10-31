// 7kyu - Complete The Pattern 2

// const pattern = n => Array.from({ length: n}, (_,i) => i + 1).reverse().join('')
// const pattern = n => Array.from({ length: n }, (_,i) => [...Array.from({ length: n}, (_,i) => i + 1).splice(i)])
// const pattern = n => Array.from({ length: n }, (_,i) => [...Array.from({ length: n}, (_,i) => i + 1).splice(i).reverse()])
const pattern = n => Array.from({ length: n }, (_, i) => [...Array.from({ length: n }, (_, i) => i + 1).splice(i).reverse()].join ``).join('\n')

// function pattern(n) {
//     let m = '';
//     return Array.from({ length: n }, () => (m = m + n--)).reverse().join('\n');
// }


q = pattern(1) // "1"
q
q = pattern(2) // "21\n2"
q
q = pattern(5) // "54321\n5432\n543\n54\n5"
q