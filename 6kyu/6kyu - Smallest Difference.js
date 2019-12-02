// 6kyu - Smallest Difference

/* Given two arrays of integers, find the pair of values with the smallest difference and return that difference.
If both arrays are empty, return -1.
If one array is empty, return the smallest value from the non-empty array.
Note: Try to solve this without brute force.

  arr1 = [1, 3, 5, 23, 5]
  arr2 = [45, 34, 67, 2, 0]
  Output = 1

  arr1 = [1, 3, 5, 23, 5]
  arr2 = []
  Output = 1

  arr1 = []
  arr2 = []
  Output = -1

Fundamentals | Arrays | Algorithm */

// function smallestDiff(arr1, arr2) {
//     let a = arr1.sort((a, b) => a - b).filter((v, i, x) => x.indexOf(v) == i)
//     let b = arr2.sort((a, b) => a - b).filter((v, i, x) => x.indexOf(v) == i)
//     let i = 0, j = 0, res = Infinity
//     if (!arr1.length && !arr2.length) return -1
//     if (!arr2.length) return a[0]
//     if (!arr1.length) return b[0]
//     while (i < a.length && j < b.length) {
//         if (Math.abs(a[i] - b[j]) < res)
//             res = Math.abs(a[i] - b[j]);
//         if (a[i] < b[j]) i++
//         else j++
//     }
//     return res
// }

function smallestDiff(arr1, arr2) {
    let i = 0, j = 0, res = Infinity
    arr1.sort((a, b) => a - b)
    arr2.sort((a, b) => a - b)
    if (!arr1.length && !arr2.length) return -1
    if (!arr2.length) return arr1[0]
    if (!arr1.length) return arr2[0]
    while (i < arr1.length && j < arr2.length) {
        if (Math.abs(arr1[i] - arr2[j]) < res)
            res = Math.abs(arr1[i] - arr2[j]);
        if (arr1[i] < arr2[j]) i++
        else j++
    }
    return res
}

// function smallestDiff(arr1, arr2) {
//     if (!arr1.length && !arr2.length) return -1
//     arr1.sort((a, b) => a - b)
//     arr2.sort((a, b) => a - b)
//     if (!arr1.length) return arr2[0]
//     if (!arr2.length) return arr1[0]
//     let i = 0, j = 0, mindiff = Infinity
//     while (i < arr1.length && j < arr2.length) {
//         let x = arr1[i], y = arr2[j]
//         mindiff = Math.min(mindiff, Math.abs(x - y))
//         if (x < y) i++
//         else j++
//     }
//     return mindiff
// }

// function smallestDiff(arr1, arr2) {
//     let diff = +Infinity;
//     if (!arr1.length && !arr2.length) return -1
//     if (!arr1.length || !arr2.length) return Math.min(...arr1.concat(arr2))
//     arr1.forEach(v1 => arr2.forEach(v2 => (d = Math.abs(v2 - v1)) < diff ? diff = d : null))
//     return diff
// }

// const smallestDiff = (a, b) => !a.length && !b.length ? -1 :
//                                !a.length ? Math.min(...b) :
//                                !b.length ? Math.min(...a) :
//                                Math.min(...a.map(e => Math.min(...b.map(f => Math.abs(e - f)))));

let min = 0;
let arr1 = [1, 3, 5, 23, 5];
let arr2 = [45, 34, 67, 2, 0];
let longArr = [23, 4, 4, 2, 5, 6, 3434, 5, 7788, 3, 2, 45, 2, 56, 78, 89, 900, 2, 3, 4, 5, 6, 7, 8, 10, 5, 7, 23, 2222, 45, 34, 56, 56, 23, 45, 56, 45454, 33, 45, 12, 16, 23, 2, 67, 78, 7, 99, 31, 27, 14, 13, 56, 72, 2, 78, 89, 34, 33, 2, 22, 55, 6, 22, 19, 45, 37, 19, 10, 2, 3, 4, 9];
let negArr = [-3, -1, -5, -56];

q = smallestDiff([], []) // -1
q
q = smallestDiff(arr1, []) // 1
q
q = smallestDiff(arr2, []) // 0
q
q = smallestDiff(arr1, arr2) // 1
q
q = smallestDiff(arr1, longArr) // 0
q
q = smallestDiff(negArr, longArr) // 3
q