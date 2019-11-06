/* 7kyu - Power of 4

Write a method that returns true if a given parameter is a power of 4, and false if it's not. 
If parameter is not an Integer (eg String, Array) method should return false as well. */

// function powerOf4(n) {
//     if (!Number.isInteger(n) || n == 0 || n == 1)
//         return false
//     while (n != 1) {
//         if (n % 4 != 0)
//             return false
//         n = n / 4
//     }
//     return true
// }

// function powerOf4(n) {
//     if (n < 2) return false
//     while (n >= 4) n /= 4
//     return n == 1
// }

const powerOf4 = n => (n < 4 || n % 4 !== 0) ? false : Number.isInteger(n)

// const powerOf4 = n => n !== (n | 0) ? false : /^10+$/.test(n.toString(4))

o = (4096).toString(4)
o

q = powerOf4(4) // true
q
q = powerOf4(16) // true
q
q = powerOf4(1) // false
q
q = powerOf4(3.1415) // false
q
q = powerOf4("4") // false
q
q = powerOf4(null) // false
q
q = powerOf4(undefined) // false
q
q = powerOf4(function () {}) // false
q