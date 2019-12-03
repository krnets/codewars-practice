// 7kyu - Smallest Product

/* Given an array of arrays, multiply the contents of each nested array and return the smallest total.

Note: all inputs will be positive integers.

Example: input [[1,5],[2]] output: 2 */

const smallestProduct = arr => Math.min(...arr.map(v => v.reduce((a, b) => a * b, 1)))

// const smallestProduct = arr => arr.reduce((s, v) => Math.min(s, v.reduce((a, b) => a * b)), Infinity)


q = smallestProduct([[3, 2],[1, 2, 1],[7, 8]]) // 2
q