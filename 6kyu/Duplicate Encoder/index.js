// 6kyu - Duplicate Encoder

/* The goal of this exercise is to convert a string to a new string where each character 
in the new string is "(" if that character appears only once in the original string, 
or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

Assertion messages may be unclear about what they display in some languages. 
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input! */

// function duplicateEncode(word) {
//     let res = ''
//     let w = word.toLowerCase()
//     let dups = [...w].filter((v, i) => w.indexOf(v) != i)
//     for (let i = 0; i < word.length; i++) {
//         if (dups.includes(w[i])) res += ')'
//         else res += '('
//     }
//     return res
// }

// const duplicateEncode = (word) => [...word.toLowerCase()].map((v, _, a) => a.indexOf(v) == a.lastIndexOf(v) ? '(' : ')').join('')
const duplicateEncode = (word) => (w = word.toLowerCase(), w.replace(/./g, v => w.indexOf(v) == w.lastIndexOf(v) ? '(' : ')'))

q = duplicateEncode("din") // "((("
q
q = duplicateEncode("recede") // "()()()"
q
q = duplicateEncode("Success") // ")())())","should ignore case"
q
q = duplicateEncode("(( @") // "))(("
q