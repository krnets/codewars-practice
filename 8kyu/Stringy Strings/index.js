// 8kyu - Stringy Strings

/* Write a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
the string should start with a 1.
a string with size 6 should return :'101010'.
with size 4 should return : '1010'.
with size 12 should return : '101010101010'.
The size will always be positive and will only use whole numbers. */

// function stringy(size) {
//     let output = ''
//     for (let i = 0; i < size; i++) {
//         if (i % 2 == 0) output += '1'
//         else output += '0'
//     }
//     return output
// }

// const stringy = (size) => "10".repeat(size).slice(0,size)

const stringy = (size) => ''.padStart(size, '10');

q = stringy(1)
q
q = stringy(2)
q
q = stringy(5)
q
q = stringy(12)
q