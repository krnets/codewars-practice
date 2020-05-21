// 7kyu - Reverse list

// const reverseList = arr => arr.reverse()
// const reverseList = Function.call.bind(Array.prototype.reverse)
// const reverseList = arr => arr.map((_, i) => arr[arr.length - 1 - i])

// function reverseList(arr) {
//     let reversed = []
//     for (let i = arr.length - 1; i >= 0; i--)
//         reversed.push(arr[i])
//     return reversed
// }

// function reverseList(arr) {
//     let reversed = []
//     for (let i of arr)
//         reversed.unshift(i)
//     return reversed
// }

// const reverseList = arr => arr.length ? reverseList(arr.slice(1)).concat(arr[0]) : arr
const reverseList = arr => !!arr && arr.length ? reverseList(arr.slice(1)).concat(arr[0]) : []

// const reverseList = arr => (xs => xs.length < 1 ? [] : [xs.pop(), ...reverseList(xs)])(arr.slice())
// const reverseList = arr => (xs => xs.length ? [xs.pop(), ...reverseList(xs)] : [])(arr.slice())


q = reverseList([]) // []
q
q = reverseList([1, 2, 3]) // [3, 2, 1]
q
q = reverseList() // []
q