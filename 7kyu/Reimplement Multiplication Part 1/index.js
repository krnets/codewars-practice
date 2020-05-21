// 7kyu - Reimplement Multiplication Part 1

/* Define a function mul(a, b) that takes two non-negative integers a and b and returns their product.

You should only use the + and/or - operators. Using * is cheating!

You can do this iteratively or recursively. */

const mul = (a, b) => b ? a + mul(a, b - 1) : 0

// function mul(a, b) {
//     let product = 0;
//     for (let i = 0; i < b; i++)
//         product += a;
//     return product;
// }

q = mul(1, 0) //  0
q
q = mul(0, 1) //  0
q
q = mul(1, 0) //  0
q
q = mul(1, 1) //  1
q
q = mul(2, 2) //  4
q
q = mul(5, 5) // 25
q