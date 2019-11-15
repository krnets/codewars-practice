// 7kyu - Evens times last

/* Given an array of integers, return the sum of all the integers 
that have an even index, multiplied by the integer at the last index.

If the array is empty, you should return 0. */


const evenLast = numbers => numbers.reduce((acc, c, i) => i % 2 == 0 ? acc + c : acc, 0) * numbers.slice(-1)

q = evenLast([2, 3, 4, 5]) // 30
q
q = evenLast([]) // 0
q