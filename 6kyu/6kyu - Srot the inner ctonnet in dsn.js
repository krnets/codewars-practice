// 6kyu - Srot the inner ctonnet in dsnnieedcg oredr

/* You have to sort the inner content of every word of a string in descending order.
The inner content is the content of a word without first and the last char.

The string will never be null and will never be empty.
It will contain only lowercase-letters and whitespaces. */

// function sortTheInnerContent(words) {
//     let a = words.split(' ')
//     return a.map(v => v[0] + [...v.slice(1, -1)].sort().reverse().join('') + v.slice(-1)).join(' ')
// }

// const sortTheInnerContent = words => words.split(' ').map(v => v.length > 1 ? v[0] + [...v.slice(1, -1)].sort().reverse().join('') + v.slice(-1) : v).join(' ')

const sortTheInnerContent = words => words.replace(/\B\w+\B/g, s => [...s].sort().reverse().join(''))

q = sortTheInnerContent("sort the inner content in descending order") // "srot the inner ctonnet in dsnnieedcg oredr"
q
q = sortTheInnerContent("wait for me") // "wiat for me"
q
q = sortTheInnerContent("this kata is easy") // "tihs ktaa is esay"
q