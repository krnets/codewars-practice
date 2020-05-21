// 7kyu - More than one way to call a function, or skin a cat

/* Write a single function that can be invoked by either

sum(2,3); //5 
sum(2)(3); //5

Both of these examples should return the sum of the 2 numbers. */

// function sum(a, b) {
//     if (arguments.length == 1) {
//         return function (b) {
//             return a + b
//         }
//     }
//     return a + b
// }

function sum(a, b) {
    return 1 in arguments ? a + b : b => a + b
}

// const sum = (a, b) => b == undefined ? b => a + b : a + b

q = sum(2, 3) == 5 // 5
q
q = sum(3)(3) == 6 // 5
q