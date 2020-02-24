// 5kyu - Maximum Subarray Sum II

/* Take a look to the kata Maximum Subarray Sum https://www.codewars.com/kata/maximum-subarray-sum 
In that kata (if you solved it), you had to give the maximum value of the elements of all the subarrays.

In this kata, we have a similar task but you have to find the sub-array or sub-arrays having this 
maximum value for their corresponding sums of elements. The wanted function: findSubarrMaxSum()

find_subarr_maxsum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [[4, -1, 2, 1], 6]

If in the solution we have two or more arrays having the maximum sum value, the result will have 
an array of arrays in the corresponding order of the array, from left to right.

find_subarr_maxsum([4, -1, 2, 1, -40, 1, 2, -1, 4]) == [[[4, -1, 2, 1], [1, 2, -1, 4]], 6]  
# From left to right [4, -1, 2, 1] appears in the array before than [1, 2, -1, 4].

If the array does not have any sub-array with a positive sum of its terms, the function will return [[], 0]. */

// function findSubarrMaxSum(arr) {
//     let maxSum = 0
//     let result = []
//     for (let i = 0; i < arr.length; i++) {
//         for (let j = 1; j <= arr.length; j++) {
//             let subArr = arr.slice(i, j)
//             let subSum = subArr.reduce((a, b) => a + b, 0)
//             if (subSum > maxSum) {
//                 maxSum = subSum
//             }
//             result.push([subArr, subSum])
//         }
//     }
//     result = result.filter(v => v[1] == maxSum).map(v => v[0]).filter(v => v.length)
//     return result.length == 1 ? result.concat(maxSum) : [result, maxSum]
// }


function findSubarrMaxSum(arr) {
    let max = 0
    let res = []
    for (let i = 0; i < arr.length; i++) {
        for (let j = 1; i + j <= arr.length; j++) {
            let sub = arr.slice(i, i + j)
            let subSum = sub.reduce((a, b) => a + b, 0)
            if (subSum > max) {
                max = subSum
                res = []
            }
            if (subSum == max) {
                res.push(sub)
            }
        }
    }
    return [(res.length == 1 ? res[0] : res), max]
}

// function findSubarrMaxSum(arr) {
//     let min = 0
//     let max = 0
//     let maxIdx = [-1]
//     let ranges = [[]]
//     for (let i = 0, sum = 0; i < arr.length; i++) {
//         sum += arr[i]
//         if (sum - min > max) {
//             max = sum - min, ranges = maxIdx.map(j => [j, i])
//         } else if (sum - min == max) {
//             ranges.push(...maxIdx.map(j => [j, i]))
//         }
//         if (sum < min) {
//             min = sum, maxIdx = [i]
//         } else if (sum == min) {
//             maxIdx.push(i)
//         }
//     }
//     if (ranges[0].length) {
//         ranges = ranges.map(([i, j]) => arr.slice(i + 1, j + 1))
//         return (ranges.length > 1 ? [ranges] : ranges).concat(max)
//     }
//     return [[], 0]
// }

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
q = findSubarrMaxSum(arr) // [[4, -1, 2, 1], 6]
q

arr = [4, -1, 2, 1, -40, 1, 2, -1, 4];
q = findSubarrMaxSum(arr) // [[[4, -1, 2, 1], [1, 2, -1, 4]], 6]
q

arr = [-4, -1, -2, -1, -40, -1, -2, -1, -4];
q = findSubarrMaxSum(arr) // [[], 0]
q

arr = [2, 1, 3, 4, 1, 2, 1, 5, 4];
q = findSubarrMaxSum(arr) // [[2, 1, 3, 4, 1, 2, 1, 5, 4], 23]
q