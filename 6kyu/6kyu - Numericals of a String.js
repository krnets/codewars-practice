// 6kyu - Numericals of a String

/* You are given an input string.

For each symbol in the string if it's the first character occurence, replace it with a '1', else replace it with the amount of times you've already seen it...

But will your code be performant enough?
Examples:

input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"

There might be some non-ascii characters in the string. */

// function numericals(s) {
//     let dict = {};
//     let res  = [];
//     [...s].forEach(v => { (dict[v] = dict[v] + 1 || 0); res.push(dict[v] + 1) })
//     return res.join ``
// }

// const numericals = (str, seen = {}) => str.replace(/./g, char => seen[char] = (seen[char] || 0) + 1)

// function numericals(s) {
//     const count = {}
//     return [...s].map(c => count[c] = ++count[c] || 1).join ``
// }

// const numericals = (s, count = {}) => [...s].map(c => count[c] = ++count[c] || 1).join ``
const numericals = (s, count = {}) => s.replace(/./g, c => count[c] = ++count[c] || 1)
// const numericals = (s, count = {}) => s.replace(/./g, c => {if (!count[c]) count[c] = 0; return ++count[c]})


q = numericals("Hello, World!") // "1112111121311"
q
q = numericals("Hello, World! It's me, JomoPipi!") // "11121111213112111131224132411122"
q
q = numericals("hello hello") // "11121122342"
q
q = numericals("Hello") // "11121"
q
q = numericals("aaaaaaaaaaaa") // "123456789101112"
q