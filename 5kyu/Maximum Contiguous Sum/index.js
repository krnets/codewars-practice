// 5kyu - Maximum Contiguous Sum

/* Given an unsorted array of integer values, find the maximum positive sum of any contiguous range within the array.

An array containing only negative values can return 0. Your solution should be efficient enough to not throw a timeout exception.
Example:

maxContiguousSum([3, -4, 8, 7, -10, 19, -3]); // returns 24
maxContiguousSum([-8, -10, -12, -2, -3, 5]); // returns 5

Visual example:

[3, -4, 8, 7, -10, 19, -3]
       |_____________|
             ||
             \/
             24      */

// function maxContiguousSum(arr) {
//     let min = 0, sum = 0, ans = 0
//     for (let i = 0; i < arr.length; i++) {
//         sum += arr[i]
//         min = Math.min(min, sum)
//         ans = Math.max(ans, sum - min)
//     }    
//     return ans
// }

// const maxContiguousSum = (arr, sum = 0) => arr.reduce((max, n) => (sum = Math.max(sum + n, 0), Math.max(c, max)), 0)
const maxContiguousSum = (arr, sum = 0) => arr.reduce((max, n) => Math.max(sum = Math.max(sum + n, 0), max), 0)

q = maxContiguousSum([3, -4, 8, 7, -10, 19, -3]) // 24
q
q = maxContiguousSum([2, -3, -3, 9, -29, 8, -9]) // 9
q