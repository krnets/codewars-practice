// 6kyu - Element equals its index

/* Given a sorted array of distinct integers, write a function indexEqualsValue that returns 
the lowest index for which array[index] == index.
Return -1 if there is no such index.

Your algorithm should be very performant.

[input] array of integers ( with 0-based nonnegative indexing )
[output] integer
Examples:

input: [-8,0,2,5]
output: 2 # since array[2] == 2

input: [-1,0,3,6]
output: -1 # since no index in array satisfies array[index] == index

Random Tests Constraints:

Array length: 200 000
Amount of tests: 1 000
Time limit: 150 ms */

// function indexEqualsValue(a) {
//     let i = 0
//     while (a[i + 100000] < 0) i += 100000
//     while (a[i + 10000] < 0) i += 10000
//     while (a[i + 1000] < 0) i += 1000
//     while (a[i + 100] < 0) i += 100
//     while (a[i + 10] < 0) i += 10
//     while (a[i] < 0) i++
//     while (a[i + 10000] < i + 10000) i += 10000
//     while (a[i + 1000] < i + 1000) i += 1000
//     while (a[i + 100] < i + 100) i += 100
//     while (a[i + 10] < i + 10) i += 10
//     while (a[i] < i) i++
//     return a[i] == i ? i : -1
// }


// function indexEqualsValue(a) {
//     let start = 0
//     let end = a.length
//     let found = -1
//     while (start < end) {
//         let index = Math.floor((start + end) / 2)
//         if (a[index] > index) {
//             end = index
//         } else if (a[index] < index) {
//             start = index + 1
//         } else {
//             found = index
//             end = index
//         }
//     }
//     return found
// }

function indexEqualsValue(a) {
    let min = 0
    let max = a.length - 1
    while (min < max) {
        let i = Math.floor((min + max) / 2)
        if (i <= a[i]) max = i
        else min = i + 1
    }
    return a[max] === max ? max : -1
}


q = indexEqualsValue([-8, 0, 2, 5]) // 2 
q
q = indexEqualsValue([-1, 0, 3, 6]) // -1 
q
q = indexEqualsValue([-3, 0, 1, 3, 10]) // 3 
q
q = indexEqualsValue([-5, 1, 2, 3, 4, 5, 7, 10, 15]) // 1 
q
q = indexEqualsValue([9, 10, 11, 12, 13, 14]) // -1 
q
q = indexEqualsValue([0]) // 0 
q