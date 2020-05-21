// 7kyu - Divide and Conquer

/* Given a mixed array of number and string representations of integers, 
add up the string integers and subtract this from the total of the non-string integers.

Return as a number.
Fundamentals | Strings | Numbers | Arrays */

// function divCon(x) {
//     let a = x.filter(v => typeof v == 'string').reduce((a, b) => a + Number(b), 0)
//     let b = x.filter(v => typeof v == 'number').reduce((a, b) => a + b, 0)
//     return b - a
// }

const divCon = (x) => x.reduce((a, b) => a + (0 + b == b ? b : -Number(b)), 0)
const divCon = (x) => x.reduce((a, b) => typeof b == 'number' ? a + b : a - Number(b), 0)


q = divCon([9, 3, '7', '3']) // 2
q
q = divCon(['5', '0', 9, 3, 2, 1, '9', 6, 7]) // 14
q
q = divCon(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']) // 13
q