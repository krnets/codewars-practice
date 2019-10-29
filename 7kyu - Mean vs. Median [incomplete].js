// 7kyu - Mean vs. Median

// function meanVsMedian(numbers) {
// let a = numbers.reduce((a, b) => a + b, 0)
// a
// let b = numbers.length
// b
// return a / b == 1 ? 'same' :
//         a / b > b ? 'mean' : 'median'
// }

// if ((a / b) == 1) {
//     return 'same'
// }

// if (a / b > b) {
//     return 'mean'
// }

// if (a / b < b) {
//     return 'median'
// }




// > numbers.length ? 'mean' :
                                // numbers.reduce((a, b) => a + b) / numbers.length == 1 ? 'same' : 'median'

q = meanVsMedian([1, 1, 1]) // 'same'
q
q = meanVsMedian([-10, 20, 5]) // 'same'
q
q = meanVsMedian([1, 2, 37]) // 'mean'
q
q = meanVsMedian([7, 14, -70]) // 'median'
q