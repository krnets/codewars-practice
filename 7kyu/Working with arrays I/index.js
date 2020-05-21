// 7kyu - Working with arrays I (and why your code fails in some katas)

/* In this kata the function returns an array/list of numbers without its last element. 
The function is already written for you and the basic tests pass, but random tests fail. 
Your task is to figure out why and fix it.

Hint: watch out for side effects.

Some good reading: MDN Docs about arrays */

// function withoutLast(arr) {
//     let clone = arr.slice()
//     clone.pop()
//     return clone
// }

const withoutLast = arr => arr.slice(0, -1)

q = withoutLast([1, 2, 3, 4, 5]) // [1, 2, 3, 4]
q
q = withoutLast([6, 7, 8, 9]) // [6, 7, 8]
q
q = withoutLast([24, 92, 99, 50, 76]) // [ 24, 92, 99, 50 ]
q