// 7kyu - Sum of a sequence

// const sequenceSum = (begin, end, step) => Array.from({length: ((end - begin) / step + 1)}, (_, i) => begin + (i * step)).reduce((a,b) => a + b, 0)

// recursive version:
const sequenceSum = (begin, end, step) => (begin > end) ? 0 : begin + sequenceSum(begin + step, end, step)

// recursive pre-ES6 version:
// function sequenceSum(begin, end, step) {
//     if (begin > end)
//         return 0
//     return begin + sequenceSum(begin + step, end, step)
// //         ^sums on return     ^constructs the range
// }


// // iterative solution # 1
// function sequenceSum(begin, end, step) {
//     let sum = 0
//     for (let i = begin; i <= end; i += step)
//         sum += i
//     return sum
// }

// // iterative solution # 2
// function sequenceSum(begin, end, step) {
//     let sum = 0
//     let index = begin
//     while (index <= end) {
//         sum = sum + index;
//         index = index + step
//     }
//     return sum
// }

// // iterative solution # 3
// function sequenceSum(begin, end, step) {
//     let sum = 0
//     let index = begin
//     do {
//         sum = sum + index
//         index = index + step
//     } while (index <= end)
//     return sum
// }

q = sequenceSum(2, 6, 2) // 12
q
q = sequenceSum(1, 5, 1) // 15
q
q = sequenceSum(1, 5, 3) // 5
q
q = sequenceSum(2, 7, 2) // 12
q
q = sequenceSum(1, 15, 3) // 15
q
q = sequenceSum(2, 25, 4) // 15
q
q = sequenceSum(3, 45, 7) // 15
q