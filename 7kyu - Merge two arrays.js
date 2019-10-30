// 7kyu - Merge two arrays

// import {compact, flatten, zip} from 'lodash'
// const mergeArrays = (a, b) => compact(flatten(zip(a, b)))

// function mergeArrays(a,b) {
//     let index = 0
//     let output = []
//     while (a[index] || b[index]) {
//         if (a[index])
//             output.push(a[index])
//         if (b[index])
//             output.push(b[index])
//         index++
//     }
//     return output
// }

// function mergeArrays(a, b) {
//     let newArray = []
//     let greaterArray = a.length >= b.length ? a : b
//     greaterArray

//     for (let i = 0; i < greaterArray.length; i++) {
//         if (a[i] === undefined) {
//             newArray.push(b[i])
//         } else if (b[i] === undefined) {
//             newArray.push(a[i])
//         } else {
//             newArray.push(a[i])
//             newArray.push(b[i])
//         }
//     }
//     return newArray
// }

function mergeArrays(a, b) {
    for (var res = [], i = 0; i < Math.max(a.length, b.length); i++) {
        if (i < a.length) res.push(a[i])
        if (i < b.length) res.push(b[i])
    }
    return res
}


// function mergeArrays(a, b) {
//     for (var res = [], i = 0; a[i] || b[i]; i++) {
//         if (a[i]) res.push(a[i])
//         if (b[i]) res.push(b[i])
//     }
//     return res
// }

let q = mergeArrays([1, 2, 3, 4, 5, 6, 7, 8], ['a', 'b', 'c', 'd', 'e']) // [1, "a", 2, "b", 3, "c", 4, "d", 5, "e", 6, 7, 8]
q
q = mergeArrays(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5]) // ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5]
q
q = mergeArrays([2, 5, 8, 23, 67, 6], ['b', 'r', 'a', 'u', 'r', 's']) // [2, 'b', 5, 'r', 8, 'a', 23, 'u', 67, 'r', 6, 's']
q
q = mergeArrays(['b', 'r', 'a', 'u', 'r', 's', 'e', 'q', 'z'], [2, 5, 8, 23, 67, 6]) // ['b', 2, 'r', 5, 'a', 8, 'u', 23, 'r', 67, 's', 6, 'e', 'q', 'z']
q