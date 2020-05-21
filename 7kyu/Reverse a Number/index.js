// 7kyu - Reverse a Number

// function reverseNumber(n) {
//     let sign = n < 0 ? '-' : ''
//     return Number(sign + ([...String(Math.abs(n))].reverse().join ``))
// }

// const reverseNumber = n => (n > 0 ? 1 : -1) * Math.abs(n).toString().split('').reverse().join('')
// const reverseNumber = n => (n > 0 ? 1 : -1) * ([...String(Math.abs(n))].reverse().join ``)
const reverseNumber = n => Math.sign(n) * ([...String(Math.abs(n))].reverse().join ``)

q = reverseNumber(123) // 321
q
q = reverseNumber(-123) // -321, 'Negative Numbers should be preserved'
q
q = reverseNumber(1000) // 1 'Should handle numbers ending with "0"'
q
q = reverseNumber(4321234) // 4321234
q
q = reverseNumber(5) // 5
q
q = reverseNumber(0) // 0
q
q = reverseNumber(98989898) // 89898989
q