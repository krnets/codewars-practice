// 7kyu - Simple remove left-most duplicates

// function solve(arr) {
//     for (var res = [], i = arr.length - 1; i >= 0; i--)
//         if (!res.includes(arr[i]))
//             res.push(arr[i])
//     return res.reverse()
// }

// const solve = arr => arr.filter((val, i) => arr.lastIndexOf(val) == i)

// const solve = arr => arr.filter((val, i) => !arr.includes(val, i + 1))

// const solve = arr => Array.from(new Set(arr.reverse())).reverse()

const solve = arr => [...new Set(arr.reverse())].reverse()

// const solve = arr => [...arr.reduceRight((acc, v) => acc.add(v), new Set)].reverse();


q = solve([3, 4, 4, 3, 6, 3]) // [4,6,3]
q
q = solve([1, 2, 1, 2, 1, 2, 3]) // [1,2,3]
q
q = solve([1, 2, 3, 4]) // [1,2,3,4]
q
q = solve([1, 1, 4, 5, 1, 2, 1]) // [4,5,2,1]
q
q = solve([1, 2, 1, 2, 1, 1, 3]) // [2,1,3]
q