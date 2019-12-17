// 6kyu - Pyramid Array

/* Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]

Note: the subarrays should be filled with 1s */

const pyramid = (n) => Array(n).fill().map((_, i) => Array(i + 1).fill(1))
// const pyramid = (n) => n == 0 ? [] : pyramid(n - 1).concat([Array(n).fill(1)])


q = pyramid(0) // []
q
q = pyramid(1) // [[1]]
q
q = pyramid(2) // [[1], [1, 1]]
q
q = pyramid(3) // [[1], [1, 1], [1, 1, 1]]
q