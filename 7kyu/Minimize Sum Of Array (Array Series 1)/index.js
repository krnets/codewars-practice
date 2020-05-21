// function minSum(arr) {
//     let sum = 0
//     arr.sort((a, b) => a - b)
//     while (arr.length > 0)
//         sum += arr.splice(0, 1) * arr.splice(-1)
//     return sum
// }

// function minSum(arr) {
//     arr.sort((a, b) => a - b)
//     let sum = 0
//     while (arr.length)
//         sum += arr.shift() * arr.pop()
//     return sum
// }

// const minSum = arr => arr.sort((a, b) => a - b)
//     .slice(0, arr.length / 2)
//     .reduce((acc, curr, index) => acc += curr * arr[arr.length - 1 - index], 0)

const minSum = arr => arr.sort((a, b) => a - b)
                        .reduce((sum, curr, index, a) => sum + curr * a[arr.length - index - 1], 0) / 2

q = minSum([5, 4, 2, 3]) // 22
q
q = minSum([12, 6, 10, 26, 3, 24]) // 342
q
q = minSum([9, 2, 8, 7, 5, 4, 0, 6]) // 74
q