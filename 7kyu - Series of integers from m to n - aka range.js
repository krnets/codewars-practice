// const generateIntegers = (m,n) => Array(n).fill().map((_,i) => m + i).filter(v => v <= n)
// const generateIntegers = (m,n) => Array.from({length: n}, (_, k) => k + 1).filter(v => v >= 2)
// const generateIntegers = (m, n) => Array.from({length: n - m + 1}, (_, i) => m + i)
const generateIntegers = (m, n) => Array(n - m + 1).fill().map(() => m++)

// const generateIntegers = (m, n) => [...Array(n)].map((_, i) => m + i).filter(v => v <= n)
// const generateIntegers = (m, n) => [...Array(n)].map((_, i) => m + i).filter(v => v <= n)

// function generateIntegers(m, n) {
//     let array = []
//     for (let i = m; i <= n; i++)
//         array.push(i)
//     return array
// }


q = generateIntegers(2, 5) // [2, 3, 4, 5]
q