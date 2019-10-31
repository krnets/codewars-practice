// 7kyu - Debug Sum of Digits of a Number

// function getSumOfDigits(integer) {
//     let sum = 0
//     let digits = String(integer)

//     for (let i = 0; i < digits.length; i++)
//         sum += +digits[i]

//     return sum
// }

const getSumOfDigits = integer => [...String(integer)].reduce((sum, d) => +d + sum, 0)

q = getSumOfDigits(123) // 6
q
q = getSumOfDigits(789) // 6
q
q = getSumOfDigits('a') // 6
q