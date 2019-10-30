// 7kyu - Top N Largest Elements

// const largest = (n, xs) => xs.sort((a, b) => b - a).slice(0, n).sort((a, b) => a - b)
const largest = (n, xs) => xs.sort((a, b) => a - b).slice(xs.length - n)
// const largest = (n, xs) => n ? xs.sort((a, b) => a - b).slice(-n) : []

q = largest(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) // [9,10]
q
q = largest(3, [5, 1, 5, 2, 3, 1, 2, 3, 5]) // [5,5,5]
q
q = largest(7, [9, 1, 50, 22, 3, 13, 2, 63, 5]) // [3, 5, 9, 13, 22, 50, 63]
q
q = largest(0, [1, 2, 3, 4, 8, 7, 6, 5]) // []
q