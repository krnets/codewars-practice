// 7kyu - Sum of all arguments

// function sum() {
//     let arr = [...arguments]
//     return arr.reduce((a, b) => a + b, 0)
// }

// function sum() {
//     let total = 0
//     for (var i in arguments)
//         total += arguments[i]
//     return total
// }

// function sum() {
//     for (var res = 0, i = 0; i < arguments.length; i++)
//         res += arguments[i]
//     return res
// }

// function sum() {
//     return Array.prototype.reduce.call(arguments, (a, b) => a + b, 0)
// }

function sum() {
    return [].reduce.call(arguments, (a, b) => a + b, 0)
}


q = sum(1, 2, 3) // => 6
q
q = sum(8, 2) // => 10
q
q = sum(1, 2, 3, 4, 5) // => 15
q