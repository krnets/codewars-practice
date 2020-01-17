// 8kyu - Triple Trouble

/* Create a function that will return a string that combines all of the letters of the three inputed strings in groups. 
Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length. */

// function tripleTrouble(one, two, three) {
//     for (var res = '', i = 0; i < one.length; i++)
//         res += one[i] + two[i] + three[i]
//     return res
// }

const tripleTrouble = (one, two, three) => one.split('').map((letter, i) => letter + two[i] + three[i]).join('')

q = tripleTrouble("this", "test", "lock") // "ttlheoiscstk"
q
q = tripleTrouble("aa", "bb", "cc") // "abcabc"
q
q = tripleTrouble("Bm", "aa", "tn") // "Batman"
q
q = tripleTrouble("LLh", "euo", "xtr") // "LexLuthor"
q