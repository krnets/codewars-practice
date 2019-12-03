// 7kyu - Largest pair sum in array

/* Given an array of numbers, find the largest pair sum in the array.
Input array contains minimum two elements and every element is a number. */

const largestPairSum = numbers => numbers.sort((a, b) => b - a)[0] + numbers[1]

q = largestPairSum([10, 14, 2, 23, 19]) // 42 (i.e. sum of 23,19)
q
q = largestPairSum([99, 2, 2, 23, 19]) // 122 (i.e. sum of 99,23)
q
q = largestPairSum([-10, -8, -16, -18, -19]) // -18
q