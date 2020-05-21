// 7kyu - Palindromes Here and There

/* An array is given with palindromic and non-palindromic numbers. 
A palindromic number is a number that is the same from a reversed order. 
For example 122 is not a palindromic number, but 202 is one.

Your task is to write a function that returns an array with only 1s and 0s, 
where all palindromic numbers are replaced with a 1 and all non-palindromic numbers are replaced with a 0. */

const convertPalindromes = (numbers) => numbers.map(v => [...String(v)].reverse().join('') == v ? 1 : 0)

q = convertPalindromes([22, 303, 76, 411, 89]) // [1, 1, 0, 0, 0]
q
q = convertPalindromes([653, 808, 5]) // [0, 1, 1]
q
q = convertPalindromes([4, 23, 441, 565, 19, 818]) // [1, 0, 0, 1, 0, 1]
q
q = convertPalindromes([101, 2, 85, 33, 14014]) //  [1, 1, 0, 1, 0]
q
q = convertPalindromes([45, 21, 303, 56]) //  [0, 0, 1, 0]
q