// 7kyu - Double Sort

/* Simple enough this one - you will be given an array. The values in the array will either be numbers or strings, 
or a mix of both. You will not get an empty array, nor a sparse one.

Your job is to return a single array that has first the numbers sorted in ascending order, followed by the strings 
sorted in alphabetic order. The values must maintain their original type.

Note that numbers written as strings are strings and must be sorted with the other strings.
Fundamentals | Strings | Numbers | Arrays */

// function dbSort(a) {
//     let nums = a.filter(v => typeof v == 'number')
//     let strs = a.filter(v => typeof v == 'string')
//     return nums.sort((a, b) => a - b).concat(strs.sort())
// }

// const dbSort = array => array.sort((a, b) => (typeof (a) == 'string') - (typeof (b) == 'string') || (a > b) - (a < b))

const dbSort = array => array.sort((a, b) => !b.split - !a.split || b < a || -1)

q = dbSort([6, 2, 3, 4, 5]) // [2, 3, 4, 5, 6]
q
q = dbSort([14, 32, 3, 5, 5]) // [3, 5, 5, 14, 32]
q
q = dbSort([1, 2, 3, 4, 5]) // [1, 2, 3, 4, 5]
q
q = dbSort(["Banana", "Orange", "Apple", "Mango", 8, 2, 2]) // [2,2,8,"Apple","Banana","Mango","Orange"]
q
q = dbSort(["C", "W", "W", "W", 1, 2, 0]) // [0,1,2,"C","W","W","W"]
q