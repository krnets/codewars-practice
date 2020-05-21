// Beta - Multiplication sequence - part 1

/* I have created a sequence such that the next number in the sequence is the value of the 2 previous numbers multiplied.

The first two numbers and 1 and 2.

1,2,2,4,8,32,... */

// function multiplication(n) {
//     let res = [1, 2, 2]
//     for (let i = 1; i < n; i++)
//         res.push(res.slice(1, -1).reduce((a, b) => a * b))
//     res.splice(1, 1)
//     return res[n]
// }

// function multiplication(n) {
//     [a, b] = [1, 2]
//     while (n--)
//         [a, b] = [b, a * b]
//     return a
// }

const multiplication = (n) => n < 2 ? n + 1 : multiplication(n - 1) * multiplication(n - 2);

q = multiplication(0) // 1
q
q = multiplication(1) // 2
q
q = multiplication(2) // 2
q
q = multiplication(3) // 4
q
q = multiplication(6) // 256
q