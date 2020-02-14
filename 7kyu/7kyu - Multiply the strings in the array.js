// 7kyu - Multiply the strings in the array

// You received an array with two strings. Create a function that will return their product as a string.

const arrMultiply = arr => arr.reduce((a, b) => a * b).toString()

// const arrMultiply = ([a, b]) => a * b + ''

q = arrMultiply(['9', '6']) // '54'
q
q = arrMultiply(['4', '5']) // "20"
q
q = arrMultiply(['2', '-5']) // "-10"
q
q = arrMultiply(['9', '0']) // "0"
q
