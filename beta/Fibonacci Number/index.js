// Beta - Fibonacci Number

// const fib = n => n == 0 ? 0 : n == 1 ? 1 : fib(n - 1) + fib(n - 2)

// function fib(n) {
//     let acc = {}
//     let f = n => (acc[n] ? acc[n] : n <= 1 ? acc[n] = n : acc[n] = f(n - 1) + f(n - 2), acc[n])
//     return f(n)
// }

// let fib = (steps, a = 0, b = 1) => steps == 0 ? a : fib(steps - 1, b, a + b)

// function fib(steps) {
//     let fibNum = [0, 1]
//     for (var i = 0; i < steps; i++)
//         fibNum.push(fibNum[i] + fibNum[i + 1])
//     return fibNum[i]
// }

var fib = function (steps) {
    var fibNum = [0, 1]
    var f = n => (fibNum[n] ? fibNum[n] : n <= 1 ? fibNum[n] = n : fibNum[n] = f(n - 1) + f(n - 2), fibNum[n])
    return f(steps)
}

// const fib = (n, f = 0, s = 1) => (n === 0) ? f : fib(--n, s, f + s)
// const fib = s => (f = (a, b) => s && ((s--) - 1 && f(b, a + b) || a + b))(1, 0)


// function fib(steps) {
//     [a, b] = [0, 1]
//     for (let i = 0; i < steps; i++)
//         [a, b] = [b, a + b];
//     return a
// }

// function fib(steps) {
//     [a, b] = [0, 1]
//     while (steps--)
//         [a, b] = [b, a + b]
//     return a
// }

q = fib(17) // 1597
q
q = fib(20) // 6765
q
q = fib(0) // 0
q
q = fib(4) // 3
q