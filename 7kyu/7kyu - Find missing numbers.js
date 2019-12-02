// 7kyu - Find missing numbers

/* You will get an array of numbers.
Every preceding number is smaller than the one following it.
Some numbers will be missing, for instance:

[-3,-2,1,5] //missing numbers are: -1,0,2,3,4

Your task is to return an array of those missing numbers:

[-1,0,2,3,4]

Fundamentals | Numbers | Arrays */

// function findMissingNumbers(arr) {
//     for (var range = [], i = arr[0]; i <= arr[arr.length - 1]; i++)
//         range.push(i)
//     return range.filter(v => !arr.includes(v))
// }

// function findMissingNumbers(arr) {
//     for (var range = [], i = arr[0]; i <= arr[arr.length - 1]; i++)
//         if (!arr.includes(i)) range.push(i)
//     return range
// }

// const findMissingNumbers = arr => Array.from({ length: arr[arr.length - 1] - arr[0] }, (_, i) => i + arr[0]).filter(v => !arr.includes(v))
// const findMissingNumbers = arr => Array.from({ length: Math.max(arr) - arr[0] }, (_, i) => i + arr[0]).filter(v => !arr.includes(v))
const findMissingNumbers = arr => Array(Math.max(...arr) - arr[0]).fill().map((_, i) => arr[0] + i).filter(v => !arr.includes(v))


q = findMissingNumbers([-3, -2, 1, 4]), [-1, 0, 2, 3]
q
q = findMissingNumbers([-1, 0, 1, 2, 3, 4]), []
q
q = findMissingNumbers([]), []
q