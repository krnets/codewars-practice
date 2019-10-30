// 8kyu - Merge two sorted arrays into one

// function mergeArrays(a, b) {
//     for (var res = [], i = 0; i < Math.max(a.length, b.length); i++) {
//         if (i < a.length) res.push(a[i])
//         if (i < b.length) res.push(b[i])
//     }
//     return res.sort((a, b) => a - b).filter((v, i) => res.indexOf(v) == i)
// }

// const mergeArrays = (arr1, arr2) => Array.from(new Set(arr1.concat(arr2).sort((a, b) => (a - b))))
// const mergeArrays = (arr1, arr2) => [...new Set(arr1.concat(arr2))].sort((a, b) => (a - b))

import { sortBy, union } from 'lodash'

// function mergeArrays(arr1, arr2) {
//     return sortBy(union(arr1, arr2));
// }

const mergeArrays = (arr1, arr2) => sortBy(union(arr1, arr2))


let q = mergeArrays([1, 2, 3, 4], [5, 6, 7, 8]) // [1,2,3,4,5,6,7,8], "Basic tests"
q
q = mergeArrays([1, 3, 5, 7, 9], [10, 8, 6, 4, 2]) // [1,2,3,4,5,6,7,8,9,10], "Basic tests"
q
q = mergeArrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]) // [1,2,3,4,5,7,9,10,11,12], "Basic tests"
q