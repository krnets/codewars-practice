// 7kyu - Find duplicated number in consecutive unsorted list

const findDup = arr => arr.filter((v,i) => arr.indexOf(v) != i)[0]
// const findDup = arr => arr.reduce((n,v,i) => arr.indexOf(v) == i ? n : v, null)
// const findDup = arr => arr.find(v => arr.indexOf(v) != arr.lastIndexOf(v))
// const findDup = arr => arr.find(num => arr.filter(v => v === num).length === 2)
// const findDup = arr => arr.sort((a, b) => a - b).find((x, i, xs) => x === xs[i + 1])

// stack overflow if no duplicate exist:
// const findDup = arr => arr.slice(1).indexOf(arr[0]) !== -1 ? arr[0] : findDup(arr.slice(1))

// iterative solutions:
//
// function findDup(arr) {
//     arr.sort()
//     for (let i = 0; i < arr.length; i++)
//         if (arr[i] == arr[i + 1])
//             return arr[i]
// }

// function findDup(arr) {
//     let duplicate
//     arr.forEach((v, index) => {
//         if (arr.lastIndexOf(v) !== index)
//             duplicate = v
//     })
//     return duplicate
// }

// q = null == undefined
// q
q = findDup([1, 2, 2, 3]) //  2
q
q = findDup([1, 3, 2, 5, 4, 5, 7, 6]) //  5
q
q = findDup([1, 2, 3]) //  2
q