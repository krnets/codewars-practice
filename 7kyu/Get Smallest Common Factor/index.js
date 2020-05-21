// 7kyu - Get Smallest Common Factor

/* Given an array of integers, return the smallest common factors of all integers in the array.
The smallest is the number above 1 that can divide all numbers in the array without a remainder.
If there is no common factors above 1, return 1 (technically 1 is always a common factor). */

// function scf(array) {
//     for (let i = 2; i <= Math.min(...array); i++)
//         if (array.every(n => n % i == 0))
//             return i
//     return 1
// }

// Greatest common divisor
const gcd = (a, b) => a ? gcd(b % a, a) : b
// Smallest factor of n
const fct = (n, f = 2) => n % f ? fct(n, f + 1) : f
// Smallest common factor
const scf = arr => fct(arr.reduce(gcd))

q = scf([200, 30, 18, 8, 64, 34]) // 2
q
q = scf([21, 45, 51, 27, 33]) // 3
q
q = scf([133, 147, 427, 266]) // 7
q
q = fct(33)
q