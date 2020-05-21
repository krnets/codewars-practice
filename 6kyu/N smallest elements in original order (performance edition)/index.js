// 6kyu - N smallest elements in original order

/* Your task is to write a function that does just what the title suggests 
(so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there) 
with an array/list/vector of integers and the expected number n of smallest elements to return.

Also:

    the number of elements to be returned cannot be higher than the array/list/vector length;
    elements can be duplicated;
    in case of duplicates, just return them according to the original order (see third example for more clarity).

Same examples and more in the test cases:

firstNSmallest([1,2,3,4,5],3) === [1,2,3] //well, not technically ===, but you get what I mean
firstNSmallest([5,4,3,2,1],3) === [3,2,1]
firstNSmallest([1,2,3,4,1],3) === [1,2,1]
firstNSmallest([1,2,3,-4,0],3) === [1,-4,0]
firstNSmallest([1,2,3,4,5],0) === [] */


// function firstNSmallest(array, n) {
//     let result = []
//     let sorted = array.slice().sort((a, b) => a - b).slice(0, n)
//     for (let x of array)
//         if (sorted.includes(x))
//             result.push(...sorted.splice(sorted.indexOf(x), 1))
//     return result
// }

// function firstNSmallest(array, n) {
//     while (array.length != n)
//         array.splice(array.lastIndexOf(Math.max(...array)), 1)
//     return array
// }

// const firstNSmallest = (arr, n) => arr.map((e, i) => ({e,i}))
//         .sort((a, b) => a.e - b.e || a.i - b.i)
//         .slice(0, n)
//         .sort((a, b) => a.i - b.i)
//         .map(w => w.e)

// const firstNSmallest = (arr, n) => arr.map((e, i) => ({num: e, index: i}))
//         .sort((a, b) => a.num - b.num || a.index - b.index)
//         .slice(0, n)
//         .sort((a, b) => a.index - b.index)
//         .map(w => w.num)

const firstNSmallest = (arr, n) => arr.map((num, index) => ({num, index}))
        .sort((a, b) => a.num - b.num || a.index - b.index)
        .slice(0, n)
        .sort((a, b) => a.index - b.index)
        .map(w => w.num)

// const firstNSmallest = (arr, n) => arr.map((e, i) => [e, i])
//     .sort((a, b) => a[0] - b[0] || a[1] - b[1])
//     .slice(0, n)
//     .sort((a, b) => a[1] - b[1])
//     .map(v => v[0]) 

q = firstNSmallest([-2, -4, -5, 4, 1, -1, 4, 6, 7, 7, -6], 10)
// [-2, -4, -5, 4, 1, -1, 4, 6, 7, -6]
q
q = firstNSmallest([1, 2, 3, 4, 5], 3) // [1, 2, 3]
q
q = firstNSmallest([5, 4, 3, 2, 1], 3) // [3, 2, 1]
q
q = firstNSmallest([1, 2, 3, 1, 2], 3) // [1, 2, 1]
q
q = firstNSmallest([1, 2, 3, -4, 0], 3) // [1, -4, 0]
q
q = firstNSmallest([1, 2, 3, 4, 5], 0) // []
q
q = firstNSmallest([1, 2, 3, 4, 5], 5) // [1, 2, 3, 4, 5]
q
q = firstNSmallest([1, 2, 3, 4, 2], 4) // [1, 2, 3, 2]
q
q = firstNSmallest([2, 1, 2, 3, 4, 2], 2) // [2, 1]
q
q = firstNSmallest([2, 1, 2, 3, 4, 2], 3) // [2, 1, 2]
q
q = firstNSmallest([2, 1, 2, 3, 4, 2], 4) // [2, 1, 2, 2]
q