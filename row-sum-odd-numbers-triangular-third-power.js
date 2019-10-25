// function rowSumOddNumbers(n) {
//     let sum = 0
//     if (n <= 1) {
//         return 1
//     } else {
//         let oddNumber = n * (n - 1) + 1
//         for (let i = 0; i < n; i++) {
//             sum += oddNumber
//             oddNumber += 2
//         }
//         return sum
//     }
// }

const rowSumOddNumbers = (n) => Math.pow(n, 3)

const assertEquals = (fn, cmp) => fn == cmp

q = assertEquals(rowSumOddNumbers(1), 1);
q
q = rowSumOddNumbers(1) // 1
q
q = rowSumOddNumbers(2) // 8
q
q = rowSumOddNumbers(3) // 27
q
q = rowSumOddNumbers(4) // 64 
q
q = rowSumOddNumbers(5) // 125 
q
q = assertEquals(rowSumOddNumbers(42), 74088);
q