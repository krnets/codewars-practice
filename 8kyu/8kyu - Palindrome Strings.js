// 8kyu - Palindrome Strings

/* A palindrome is a word, phrase, number, or other sequence of characters which 
reads the same backward or forward. This includes capital letters, punctuation, and word dividers.

Implement a function that checks if something is a palindrome. */

// function isPalindrome(line) {
//     let s = String(line)
//     for (let i = 0, j = s.length - 1; i < s.length / 2; i++, j--)
//         if (s[i] != s[j])
//             return false
//     return true
// }

// const isPalindrome = (line) => String(line).split('').reverse().join('') == line
const isPalindrome = (line) => Array.from(line).reverse().join('') == line

q = isPalindrome("anna") // true
q
q = isPalindrome("walter") // false
q
q = isPalindrome(12321) // true
q
q = isPalindrome(123456) // false
q
q = isPalindrome(".") // true
q
q = isPalindrome(".!!.") // true
q