// 5kyu - Maximum subarray sum

/* The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence 
in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
// should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray. */


// function maxSequence(arr) {
//     let maxSum = 0
//     for (let i = 0; i < arr.length; i++) {
//         for (let j = 1; j <= arr.length; j++) {
//             let subarr = arr.slice(i, j).reduce((a, b) => a + b, 0)
//             if (subarr > maxSum) {
//                 maxSum = subarr
//             }
//         }
//     }
//     return maxSum > 0 ? maxSum : 0
// }

function maxSequence(arr) {
    let min = 0, sum = 0, ans = 0
    for (let i = 0; i < arr.length; i++) {
       sum += arr[i] 
       min = Math.min(min, sum)
       ans = Math.max(ans, sum - min)
    }
    return ans
}

// function maxSequence(arr) {
//     let currentSum = 0
//     return arr.reduce((maxSum, n) => {
//         currentSum = Math.max(currentSum + n, 0)
//         return Math.max(currentSum, maxSum)
//     }, 0)
// }

// const maxSequence = (arr, sum = 0) => arr.reduce((max, v) => Math.max(sum = Math.max(sum + v, 0), max), 0)

// function maxSequence(arr) {
//     var max = 0;
//     var cur = 0;
//     arr.forEach(function (i) {
//         cur = Math.max(0, cur + i);
//         max = Math.max(max, cur);
//     });
//     return max;
// }

q = maxSequence([]) // 0
q
q = maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) // 6
q