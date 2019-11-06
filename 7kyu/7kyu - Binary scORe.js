// 7kyu - Binary scORe


// const score = n => [...Array(n)].map((_, i) => i + 1).reduce((final, current) => final | current, 0)

const score = n => n ? Math.pow(2, n.toString(2).length) - 1 : 0

// const score = n => 2 ** Math.ceil(Math.log2(n + 1)) - 1

// function score(n) {
//     let i = 1
//     while (i < n) {
//         n |= i
//         i = i << 1
//     }
//     return n
// }

// function score(n) {
//     let i = 0
//     while (Math.pow(2, i) <= n)
//         i += 1
//     return Math.pow(2, i) - 1
// }

// function score(n) {
//     let s = 0
//     while (s < n)
//         s = s | (s + 1)
//     return s
// }

// function score(n) {
//     if (n < 2) return n
//     let res = 2
//     while (res < n) res *= 2
//     return res - 1
// }

// const score = n => n ? parseInt('1'.repeat((n).toString(2).length), 2) : 0

// The Math.clz32() function returns the number of leading zero bits in the 32-bit binary representation of a number.

// const score = n => n && -1 >>> Math.clz32(n)

q = score(0) // 0
q
q = score(1) // 1
q
q = score(49) // 63
q
q = score(1000000) // 1048575
q