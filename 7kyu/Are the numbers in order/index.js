// 7kyu - Are the numbers in order?

// const inAscOrder = arr => arr.filter((v, i) => v > arr[i + 1]).length == 0
// const inAscOrder = arr => !arr.some((_, i) => arr[i] < arr[i - 1])
// const inAscOrder = arr => arr.every((v, i) => i ? v > arr[i - 1] : !0)
// const inAscOrder = arr => arr.every((_, i) => i == 0 || arr[i] > arr[i - 1])
// const inAscOrder = arr => arr.every((v, i) => !i || v > arr[i - 1])
const inAscOrder = arr => arr.every((v, i) => v > arr[i - 1] || !i)

// function inAscOrder(arr) {
//     for (let i = 1; i < arr.length; i++) 
//         if (arr[i] < arr[i-1]) 
//             return false

//     return true
// }

q = inAscOrder([1, 2, 4, 7, 19]) // true
q
q = inAscOrder([1, 2, 3, 4, 5]) // true
q
q = inAscOrder([1, 6, 10, 18, 2, 4, 20]) // false
q
q = inAscOrder([9, 8, 7, 6, 5, 4, 3, 2, 1]) // false
q