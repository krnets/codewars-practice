// 7kyu - Flatten and sort an array

/* Given a two-dimensional array of integers, return the flattened version of the array with all 
the integers in the sorted (ascending) order.

 [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]] ->  [1, 2, 3, 4, 5, 6, 7, 8, 9]

Please, keep in mind, that JavaScript is by default sorting objects alphabetically.  */

const flattenAndSort = array => [].concat(...array).sort((a, b) => a - b)

q = flattenAndSort([]) // []
q
q = flattenAndSort([[], [1]]) // [1]
q
q = flattenAndSort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]) // [1, 2, 3, 4, 5, 6, 7, 8, 9]
q
q = flattenAndSort([[1, 3, 5], [100], [2, 4, 6]]) // [1, 2, 3, 4, 5, 6, 100]
q