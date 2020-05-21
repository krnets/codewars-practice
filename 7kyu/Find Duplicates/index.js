/* 7kyu - Find Duplicates 

Given an array, find the duplicates in that array, and return a new array of those duplicates. 
The elements of the returned array should appear in the order when they first appeared as duplicates.

Note: numbers and their corresponding string representations should not be treated as duplicates (i.e., '1' !== 1). */

const duplicates = arr => arr.filter((v, i) => arr.indexOf(v) === i && arr.lastIndexOf(v) !== i)
// const duplicates = arr => arr.reduce((acc, v, i) => arr.lastIndexOf(v) > i && acc.indexOf(v) == -1 ? [...acc, v] : acc, [])

// function duplicates(arr) {
//     for (var dupl = [], i = 0; i < arr.length; i++)
//         if (arr.indexOf(arr[i]) !== arr.lastIndexOf(arr[i]))
//             dupl.push(arr[i])
//     return dupl.filter((v, i) => dupl.indexOf(v) == i)
// }

// function duplicates(arr) {
//     for (var dupl = [], i = 0; i < arr.length; i++)
//         if (arr.indexOf(arr[i], i + 1) > 0 && dupl.indexOf(arr[i]) < 0)
//             dupl.push(arr[i])
//     return dupl
// }


q = duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']) // 3
q
q = duplicates([0, 1, 2, 3, 4, 5]) // 0
q