// 7kyu - String Merge!

/* Given two words and a letter, return a single word that's a combination of both words, 
merged at the point where the given letter first appears in each word. 
The returned word should have the beginning of the first word and the ending of the second, 
with the dividing letter in the middle. You can assume both words will contain the dividing letter. */

// function stringMerge(string1, string2, string3) {
//     return string1.slice(0, string1.indexOf(string3)) + string2.slice(string2.indexOf(string3))
// }

const stringMerge = (a, b, c) => a.slice(0, a.indexOf(c)) + b.slice(b.indexOf(c))

q = stringMerge("hello", "world", "l") //  "held"
q
q = stringMerge("jason", "samson", "s") //  "jasamson"
q
q = stringMerge("coding", "anywhere", "n") //  "codinywhere"
q
q = stringMerge("wonderful", "people", "e") //  "wondeople" 
q
q = stringMerge("person", "here", "e") // "pere"
q
q = stringMerge("apowiejfoiajsf", "iwahfeijouh", "j") // "apowiejouh"
q
q = stringMerge("abcdefxxxyzz", "abcxxxyyyxyzz", "x") // "abcdefxxxyyyxyzz"
q
q = stringMerge("12345654321", "123456789", "6") // "123456789"
q
q = stringMerge("JiOdIdA4", "oopopopoodddasdfdfsd", "d") // "JiOdddasdfdfsd"
q
q = stringMerge("incredible", "people", "e") // "increople"
q