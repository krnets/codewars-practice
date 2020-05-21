// 7kyu - Are they square?

/* Write a function that checks whether all elements in an array are square numbers. 
The function should be able to take any number of array elements.
Your function should return true if all elements in the array are square numbers and false if not.
An empty array should return undefined. You can assume that all array elements will be positive integers. */

const isSquare = (arr) => arr.length ? arr.every(v => Math.sqrt(v) % 1 == 0) : undefined

q = isSquare([1, 4, 9, 16, 25, 36]) // true
q
q = isSquare([1, 2, 3, 4, 5, 6]) // false
q
q = isSquare([]) // undefined
q
q = isSquare([1, 2, 4, 15]) // false
q