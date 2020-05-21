// 7kyu - Spoonerize Me

/* A spoonerism is a spoken phrase in which the first letters of two of the words are swapped around, often with amusing results.

In its most basic form a spoonerism is a two word phrase in which only the first letters of each word are swapped:

"not picking" --> "pot nicking"

Your task is to create a function that takes a string of two words, separated by a space: 
words and returns a spoonerism of those words in a string, as in the above example.

NOTE: All input strings will contain only two words. Spoonerisms can be more complex. 
For example, three-word phrases in which the first letters of the first and last words are swapped: 
"pack of lies" --> "lack of pies" or more than one letter from a word is swapped: 
"flat battery --> "bat flattery" You are NOT expected to account for these, or any other nuances involved in spoonerisms. */

// function spoonerize(words) {
//     let arr = words.split(' ')
//     let firstLetter = arr.map(v => v[0])
//     return arr.map((v, i) => firstLetter[arr.length - i - 1] + v.slice(1)).join(' ')
// }

// function spoonerize(words) {
//     [a, b] = words.split(' ')
//     return b[0] + a.slice(1) + ' ' + a[0] + b.slice(1)
// }

const spoonerize = (words) => words.replace(/^(.)(.* )(.)(.*)$/, '$3$2$1$4')

q = spoonerize("nit picking") // "pit nicking"
q
q = spoonerize("wedding bells") // "bedding wells"
q
q = spoonerize("jelly beans") // "belly jeans"
q