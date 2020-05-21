// 7kyu - Digit Sum

// function digitSum(str) {
//     let sum = [...str].reduce((a, b) => a + Number(b), 0).toString()
//     return sum.length == 1 ? sum : digitSum(sum)
// }

const digitSum = str => (sum => sum.length == 1 ? sum : digitSum(sum))
                        ([...str].reduce((a, b) => a + Number(b), 0).toString())

// function digitSum(str) {
//     while (str.length > 1)
//         str = [...str].reduce((a, c) => a + +c, 0).toString();
//     return str
// }


q = digitSum('1234') // '1'
q
q = digitSum('1011') // '3'
q
q = digitSum('2468') // '2'
q