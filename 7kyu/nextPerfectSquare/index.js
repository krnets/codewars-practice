// 7kyu - nextPerfectSquare

/* Write a function name nextPerfectSquare that returns the first perfect square that is greater 
than its integer argument. A perfect square is a integer that is equal to some integer squared. 
For example 16 is a perfect square because 16=4*4.

example

n   next perfect sqare

6    9
36   49 
0    1
-5   0 

caution! the largest number tested is closer to Number.MAX_SAFE_INTEGER */

// function nextPerfectSquare(n) {
//     let result = 0
//     if (n >= 0) {
//         let baseNumber = Math.floor(Math.sqrt(n))
//         let nextNumber = baseNumber + 1
//         result = Math.pow(nextNumber, 2)
//     }
//     return result
// }

const nextPerfectSquare = (n) => n < 0 ? 0 : Math.pow(Math.floor(Math.sqrt(n)) + 1, 2)
// const nextPerfectSquare = (n) => n < 0 ? 0 : ((n ** 0.5 | 0) + 1) ** 2

q = nextPerfectSquare(6) // 9
q
q = nextPerfectSquare(36) // 49
q
q = nextPerfectSquare(0) // 1
q
q = nextPerfectSquare(-5) // 0
q