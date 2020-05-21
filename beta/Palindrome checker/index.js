// Beta - Palindrome checker

/* According to Wikipedia, a palindrome is "a word, phrase, number, or other sequence of characters which 
reads the same backward or forward." Examples of palindromes include "racecar", "tacocat", and "123454321".

Capitalization, punctuation, and word dividers will be ignored when checking if a string is a palindrome. 
For example, "Was it a car or a cat I saw?" is a valid palindrome in context of this Kata.

All requirements from definition should be fulfilled.
If the given string is a palindrome, return true.
If not, or in case of null input (None for Python) return false. */

const isPalindrome = (str) => str ? (s = str.toLowerCase().replace(/\W/g, ''), s == [...s].reverse().join('')) : false

q = isPalindrome(null) // false
q
q = isPalindrome("race car") // true
q
q = isPalindrome("Amor, Roma") // true
q
q = isPalindrome("123521") // false
q