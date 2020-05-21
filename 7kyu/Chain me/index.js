// 7kyu - Chain me

/* Write a generic function chainer that takes a starting value, and an array of functions to execute on it.
The input for each function is the output of the previous function (except the first function, 
which takes the starting value as it's input). Return the final value after execution is complete. */

// function chain(input, fs) {
//     for (var res = input, i = 0; i < fs.length; i++)
//         res = fs[i](res)
//     return res
// }

const chain = (input, fs) => fs.reduce((x, f) => f(x), input)

add = (x) => x + 10
mult = (x) => x * 30
q = chain(2, [add, mult]) // 360
q

add = (num) => num + 1
mult = (num) => num * 30
q = chain(2, [add, mult]) // 90
q