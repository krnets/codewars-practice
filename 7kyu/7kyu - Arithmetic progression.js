// 7kyu - Arithmetic progression

/* Write a function that will return the first n elements of the sequence 
with the given common difference d and first element a. Note that the difference may be zero!

The result should be a string of numbers, separated by comma and space.

# first element: 1, difference: 2, how many: 5
arithmetic_sequence_elements(1, 2, 5) == "1, 3, 5, 7, 9" */

// function arithmeticSequenceElements(a, r, n) {
//     return Array.from({
//         length: n
//     }, (_, i) => a + i * r).join(', ')
// }

const arithmeticSequenceElements = (a, r, n) => [...Array(n)].map((_, i) => a + i * r).join(', ')
// const arithmeticSequenceElements = (a, r, n) => Array(n).fill().map((_, i) => a + i * r).join(', ')

// function arithmeticSequenceElements(a, r, n) {
//     var ret = [a]
//     while (--n) ret.push(a += r);
//     return ret.join(', ')
// }

q = arithmeticSequenceElements(1, 2, 5) // "1, 3, 5, 7, 9"
q
q = arithmeticSequenceElements(1, 0, 5) // "1, 1, 1, 1, 1"
q
q = arithmeticSequenceElements(1, -3, 10) // "1, -2, -5, -8, -11, -14, -17, -20, -23, -26"
q
q = arithmeticSequenceElements(100, -10, 10) // "100, 90, 80, 70, 60, 50, 40, 30, 20, 10"
q