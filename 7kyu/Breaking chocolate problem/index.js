// 7kyu - Breaking chocolate problem

// function breakChocolate(n, m) {
//     let result = n * m - 1

//     return result < 0 ? 0 : result
// }

// const breakChocolate = (n, m) => (result = n * m - 1, result < 0 ? 0 : result)
const breakChocolate = (n, m) => Math.max(0, n * m - 1)

q = breakChocolate(5, 5) // 24
q
q = breakChocolate(1, 1) // 0
q