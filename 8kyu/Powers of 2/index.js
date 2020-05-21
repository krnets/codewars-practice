/* 8kyu - Powers of 2

Complete the function that takes a non-negative integer n as input, and 
returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive). */

// const powersOfTwo = n => Array.from({ length: n + 1 }, (_, k) => Math.pow(2, k))

const powersOfTwo = n => [...Array(n + 1)].map((_, i) => 2 ** i)

q = powersOfTwo(0) // [1]
q
q = powersOfTwo(1) // [1, 2]
q
q = powersOfTwo(4) // [1, 2, 4, 8, 16]
q