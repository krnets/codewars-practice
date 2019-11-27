// Beta - Count letters in a string

// Write a function that counts the letters in a string in object notation.
// Input: A string. e.g. "Hello World" If input is anything other than a string, it should return null
// Output: Should be an object of the letters and how often they show up. e.g. { d:1 e:1 h:1 l:3 o:2 r:1 w:1 }
//     Case-insensitive. So convert all letters to lowercase
//     Ignore whitespace
//     Ignore anything not a-z


const countLetters = string => typeof string == 'string' ? [...string.replace(/[^a-z]/gi, '').toLowerCase()].reduce((dict, v) => (dict[v] = ++dict[v] || 1, dict), {}) : null
// const countLetters = string => typeof string == 'string' ? [...string.toLowerCase().replace(/[^a-z]/gi, '')].reduce((dict, v) => (dict[v] = ~~dict[v] + 1, dict), {}) : null

q = countLetters("Hello World") // { d:1 e:1 h:1 l:3 o:2 r:1 w:1 }
q