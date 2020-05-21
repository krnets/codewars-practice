// function largestPower(n) {
//     result = 0
//     while (Math.pow(3, result) < n)
//         result++
//     return result - 1
// }

const largestPower = n => Math.ceil(Math.log10(n) / Math.log10(3)) - 1

q = largestPower(3) // 0
q
q = largestPower(5) // 1
q
q = largestPower(7) // 1
q
q = largestPower(81) // 3
q
q = largestPower(82) // 4
q