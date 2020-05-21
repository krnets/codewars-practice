// Beta - Is number a palindrome?

/* Write a function which for given number returns true if number is palindrome or false if it is not.
A number is a palindrome if when the digits are reversed it is the same number.

Ex. 121 is a palindrome
121 -> 121

Ex. 345 is not a palindrome
345 => 543  */

const isPalindromic = a => a == [...String(a)].reverse().join ``

q = isPalindromic(1234567) // false
q
q = isPalindromic(2222) // true
q
q = isPalindromic(22322) // true
q
q = isPalindromic(1222222) // false
q