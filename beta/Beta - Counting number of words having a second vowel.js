// Beta - Counting number of words having a second vowel

/* Let's count the numbers of words having a second vowels in a string! 
For a given string, write a function that returns the number of words having a second vowel.

countVowels("range represented by a node is completely inside the given range") ==> 7 
countVowels("help me god") ==> 0 ; no words have a second vowel */

// const countVowels = string => string.toLowerCase().split(' ')
//     .map(word => [...word].map(ch => 'aeiou'.indexOf(ch) != -1)
//         .filter(v => v).length)
//     .filter(x => x > 1).length

// const countVowels = string => string.toLowerCase().split(' ')
//     .map(word => [...word].map(ch => 'aeiou'.includes(ch))
//         .filter(v => v).length)
//     .filter(x => x > 1).length

const countVowels = string => string.split(' ').filter(w => /[aeiou].*[aeiou]/i.test(w)).length

q = countVowels("my first kata") // 1 "The string has 1 word containing a second vowels"
q
q = countVowels("Once upon a time") // 3 "Should account for upper case elements"
q
q = countVowels("") // 0 "Empty string"
q