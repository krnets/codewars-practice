// 6kyu - Simple Fun #79: Delete a Digit

/* Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

For n = 152, the output should be 52;
For n = 1001, the output should be 101.

[input] integer n
Constraints: 10≤ n≤ 1000000.
[output] an integer */


// function deleteDigit(n) {
//     let str = String(n)
//     let res = []
//     for (let i = 0; i < str.length; i++)
//         res.push(str.slice(0, i) + str.slice(i + 1))
//     return Math.max(...res)
// }

// const deleteDigit = (n) => Math.max(...[...(s = String(n))].map((_, i) => s.slice(0, i) + s.slice(i + 1)))
const deleteDigit = (n) => Math.max(...[...(s = String(n))].map(v => s.replace(v, '')))

q = deleteDigit(152) // 52
q
q = deleteDigit(1001) // 101
q
q = deleteDigit(10) // 1
q