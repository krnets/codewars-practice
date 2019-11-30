// 7kyu - Array2Binary addition

/* Given an array containing only integers, add all the elements and return the binary equivalent of that sum.

If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.

Note: The sum of an empty array is zero. */


const arr2bin = arr => arr.every(Number.isInteger) && arr.reduce((a, b) => a + b, 0).toString(2)

q = arr2bin([1, 2]) // "11"
q
q = arr2bin([1, 2, 3, 4, 5]) // "1111"
q
q = arr2bin([1, 10, 100, 1000]) // "10001010111"
q