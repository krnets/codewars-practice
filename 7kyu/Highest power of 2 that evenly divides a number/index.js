// 7kyu - Highest power of 2 that evenly divides a number

/* Write a function that takes a number and returns highest power of 2 that evenly divides the number.

  solution( 123 ) should return 1
  solution( 192 ) => 64
  solution( 132232 ) => 8

  solution( 123 ) should return 1
  solution( 192 ) => 64
  solution( 132232 ) => 8

Assume that: number is an integer within the range [1..10^18].  */

// function solution(n) {
//     let powerOfTwo = 0
//     for (let i = 1; i <= n; i *= 2)
//         if (n % i == 0)
//             powerOfTwo = i
//     return powerOfTwo
// }

// const solution = (n) => n & -n

function solution(n) {
    let res = 1
    while (n % res == 0) res *= 2
    return res / 2
}

q = solution(123) // 1
q
q = solution(192) // 64
q
q = solution(132232) // 8
q
q = solution(64) // 64
q