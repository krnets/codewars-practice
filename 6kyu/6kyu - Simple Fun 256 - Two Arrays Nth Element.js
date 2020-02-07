// 6kyu - Simple Fun #256: Two Arrays Nth Element

/* Given two sorted arrays of integers(array1 and array2) and an integer n, find the nth (0-based) element of their sorted union.
In order to prevent brute force, array1 and array2 may contain 1000000 elements

[input] integer array array1
Sorted array of distinct integers(negative, positive or zero).
0 ≤ array1.length ≤ 1000000

[input] integer array array2
Sorted array of distinct integers(negative, positive or zero).
It is guaranteed that no integer is contained in both array1 and array2.
0 ≤ array2.length ≤ 1000000

[input] integer n
Non-negative integer less than the summary size of array1 and array2.
0 ≤ n < array1.length + array2.length

[output] an integer
The nth element(0-based).

For array1 = [1, 3, 4], array2 = [2, 6, 8] and n = 5,
the output should be 8.
Sorted union of array1 and array2 is [1, 2, 3, 4, 6, 8]. The 5th element is 8. */

// correct but times out on large input
// const twoArraysNthElement = (array1, array2, n) => array1.concat(array2).sort((a, b) => a - b)[n]

function twoArraysNthElement(arr1, arr2, n) {
    arr1.push(Infinity)
    arr2.push(Infinity)
    let i = 0
    let j = 0
    while (i + j < n) {
        arr1[i] < arr2[j] ? i++ : j++
    }
    return Math.min(arr1[i], arr2[j])
}

q = twoArraysNthElement([1, 3, 4], [2, 6, 8], 5) // 8
q
q = twoArraysNthElement([1, 3, 5], [2, 4], 2) // 3
q
q = twoArraysNthElement([1, 2, 3], [4, 5, 6], 3) // 4
q
q = twoArraysNthElement([6, 19, 21, 30, 34, 35, 44, 48], [3, 4, 5, 9, 14, 16, 25, 32, 36, 37, 41, 53], 11) // 32
q
q = twoArraysNthElement([10, 11], [4, 6], 1) // 6
q
q = twoArraysNthElement([10, 11], [4, 6], 2) // 10
q
q = twoArraysNthElement([10, 11], [4, 6], 3) // 11
q
q = twoArraysNthElement([15, 16, 21, 25, 29, 31], [5, 8, 12, 18, 28], 10) // 31
q
q = twoArraysNthElement([-6, -5, -4], [4, 5, 6], 3) // 4
q
q = twoArraysNthElement([-6, -5, -4, 0], [4, 5, 6], 3) // 0
q