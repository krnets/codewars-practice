// 6kyu - Remember

/* Write a function that takes a string and returns an array of the repeated characters (letters, numbers, whitespace) in the string.
If a charater is repeated more than once, only show it once in the result array.
Characters should be shown by the order of their first repetition. 
Note that this may be different from the order of first appearance of the character.
Characters are case sensitive. */

// const remember = (str) => Array.from(new Set([...str].filter((v, i) => str.indexOf(v) != i)))
// const remember = (str) => [...new Set([...str].filter((v, i) => str.slice(0,i).includes(v)))]
const remember = (str) => [...str].filter((v, i) => str.indexOf(v) != i).filter((v, i, arr) => arr.indexOf(v) == i)

q = remember('apple') // ["p"]
q
q = remember("apPle") // []
q
q = remember("pippi") // ["p", "i"]
q
q = remember('Pippi') // ["p", "i"]
q
q = remember("limbojackassin the garden") // ["a", "s", "i", " ", "e", "n"]
q
q = remember("11pinguin") // ["1", "i", "n"]
q