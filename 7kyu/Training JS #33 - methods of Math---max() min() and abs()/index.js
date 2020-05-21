// 7kyu - Training JS #33: methods of Math---max() min() and abs()

// function maxMin(arr1, arr2) {
//     for (var diff = [], i = 0; i < arr1.length; i++)
//         diff.push(Math.abs(arr1[i] - arr2[i]))
//     return [Math.max(...diff), Math.min(...diff)]
// }

// function maxMin(arr1, arr2) {
//     let diff = arr1.map((v, i) => Math.abs(v - arr2[i]))
//     return [Math.max(...diff), Math.min(...diff)]
// }

// const maxMin = (arr1, arr2) => [Math.max(...arr1.map((v, i) => Math.abs(v - arr2[i]))), 
//                                 Math.min(...arr1.map((v, i) => Math.abs(v - arr2[i])))]

const maxMin = (arr1, arr2) => [Math.max(...diff = arr1.map((v, i) => Math.abs(v - arr2[i]))), Math.min(...diff)]

q = maxMin([1, 3, 5], [9, 8, 7]) // [8,2]
q
q = maxMin([1, 10, 100, 1000], [0, 0, 0, 0]) // [1000,1]
q
q = maxMin([10, 20, 30, 40], [111, 11, 1, -111]) // [151,9]
q