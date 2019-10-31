// Find Multiples of a Number - 8 kyu

// const findMultiples = (integer, limit) => Array.from({length: limit}, (_, i) => integer * (i + 1)).filter(v => v <= limit)

// const findMultiples = (integer, limit) => Array(limit).fill().map((_, i) => integer * (i + 1)).filter(n => n <= limit)

// const findMultiples = (n, l) => Array.from({length: ~~(l / n)}, (_, i) => i * n + n)

// const findMultiples = (integer, limit) => [...Array(Math.floor(limit / integer))].map((_,i) => integer * (i + 1))

const findMultiples = (integer, limit) => Array(Math.floor(limit / integer)).fill().map((_, i) => integer * (i + 1))

// const findMultiples = (integer, limit) => Array(~~(limit / integer)).fill().map((_, i) => integer * (i + 1))
// function findMultiples(int,limit){
//     let result = []
    
//     for (let i = int; i<=limit ; i+=int)
//       result.push(i)
//     return result
//   }

q = 7 / 5
q
q = ~~(7 / 5)
q

// function findMultiples (integer, limit) {
//     let result = []
//     for (let i = integer; i <= limit; i += integer)
//         result.push(i)
//     return result
// }


q = findMultiples(5, 25) // [5, 10, 15, 20, 25]
q
q = findMultiples(1, 2) // [1, 2]
q
q = findMultiples(5, 7) // [5]
q
q = findMultiples(4, 27) // [4, 8, 12, 16, 20, 24]
q
q = findMultiples(11, 54) // [11, 22, 33, 44]
q