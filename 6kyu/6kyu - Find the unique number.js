// 6kyu - Find the unique number

const findUniq = arr => arr.filter(v => arr.indexOf(v) == arr.lastIndexOf(v))[0]
// const findUniq = arr => arr.find(v => arr.indexOf(v) == arr.lastIndexOf(v)) || 0

// const findUniq = arr => {
//     arr.sort((x, y) => x - y)
//     return arr.find(v => arr.indexOf(v) == arr.lastIndexOf(v)) || 0
// }

// function findUniq(arr) {
//     arr.sort((x, y) => x - y)
//     return arr[0] == arr[1] ? arr.pop() : arr[0]
// }


q = findUniq([0, 1, 0]) //  1
q
q = findUniq([1, 1, 1, 2, 1, 1]) //  2
q
q = findUniq([3, 10, 3, 3, 3]) // 10
q