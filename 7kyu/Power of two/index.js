/* 7kyu - Power of two

Complete the function powerOfTwo that determines 
if a given non-negative integer is a power of two. 

A power of two is a number of the form 2n where n is an integer, 
i.e. the result of exponentiation with number two as the base and integer n as the exponent.

You may assume the input is always valid. */

// const isPowerOfTwo = n => Number.isInteger(Math.log2(n))
// const isPowerOfTwo = n => Math.log2(n) % 1 === 0 ? true : false;
const isPowerOfTwo = n => Math.log2(n) % 1 === 0

// function isPowerOfTwo(n) {
//     if (n == 1) return true
//     if (n < 1) return false
//     return isPowerOfTwo(n / 2)
// }


q = isPowerOfTwo(2) //  true
q
q = isPowerOfTwo(4096) // true
q
q = isPowerOfTwo(5) // false
q