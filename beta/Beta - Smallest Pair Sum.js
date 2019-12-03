// Beta - Smallest Pair Sum

/* Given an array of numbers, find the smallest pair sum in the array.

[10,14,2,23,19] should return 12 (i.e. sum of 10,2)
[99,2,2,23,19] should return 4 (i.e. sum of 2,2)

Input array contains minimum two elements and every element is a number. Note :
    not all elements are distinct, and duplicates are not ignored

[1,1,2] => 1+1 = 2 */

// const smallestPairSum = arr => arr.sort((a, b) => a - b).filter((_, i) => i < 2).reduce((a, b) => a + b, 0)

// function smallestPairSum(numbers) {
//     return numbers.sort((a, b) => a - b).filter((_, i) => i < 2).reduce((a, b) => a + b, 0)
// }

// function smallestPairSum(numbers) {
//     let [min1, min2] = numbers.sort((a, b) => a - b)
//     return min1 + min2
// }

const smallestPairSum = numbers => numbers.sort((x, y) => x - y)[0] + numbers[1]

q = smallestPairSum([10, 14, 2, 23, 19]) // 12 , "Sum should be 12"
q
q = smallestPairSum([-100, -29, -24, -19, 19]) // -129 , "Sum should be -129"
q
q = smallestPairSum([1, 2, 3, 4, 6, -1, 2]) // 0 , "Sum should be 0"
q
q = smallestPairSum([-10, -8, -16, -18, -19]) // -37 , "Sum should be -37"
q