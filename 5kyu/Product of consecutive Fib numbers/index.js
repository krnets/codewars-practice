// 5kyu - Product of consecutive Fib numbers

// const fib = n => n == 0 || n == 1 ? 1 : fib(n -1) + fib (n -2)
// const fibUntil = n => n == 0 || n == 1 ? 1 : fib(n -1) + fib (n -2)

// function fib(steps) {
//     [a, b] = [0, 1]
//     while (steps--)
//         [a, b] = [b, a + b]
//     return a
// }

// function fibUntil(n) {
//     [a, b] = [0, 1]
//     while (a < n)
//         [a, b] = [b, a + b]
//     return a
// }

// function fibUntil(n) {
//     const res = [0, 1]
//     while (res[res.length - 1] < n)
//         res.push(res.slice(-2).reduce((a, b) => a + b))
//     return res.slice(-Math.ceil(res.length / 4))
// }

// function productFib(prod) {
//     let a = fibUntil(Math.round(Math.sqrt(prod) * 2))
//     for (let i = 0; a.length - 1; i++) {
//         let innerProduct = a[i] * a[i + 1]
//         if (innerProduct > prod) 
//             return [a[i], a[i + 1], false]
//         if (innerProduct == prod) 
//             return [a[i], a[i + 1], true]
//     }
// }

// function productFib(prod) {
//     let res = [0, 1]

//     while (res[res.length - 1] < ~~(Math.sqrt(prod) * 2))
//         res.push(res.slice(-2).reduce((a, b) => a + b))

//     res.slice(-Math.ceil(res.length / 4))

//     for (let i = 0; i < res.length - 1; i++) {
//         let innerProduct = res[i] * res[i + 1]
//         if (innerProduct > prod)
//             return [res[i], res[i + 1], false]
//         if (innerProduct == prod)
//             return [res[i], res[i + 1], true]
//     }
// }

function productFib(prod) {
    let [a, b] = [0, 1]
    while (a * b < prod)
        [a, b] = [b, a + b]
    return [a, b, a * b == prod]
}

q = productFib(4895) // [55, 89, true]
q
q = productFib(5895) // [89, 144, false]
q
q = productFib(74049690) // [6765, 10946, true]
q
q = productFib(84049690) // [10946, 17711, false]
q
q = productFib(193864606) // [10946, 17711, true]
q
q = productFib(447577) // [610, 987, false]
q
q = productFib(602070) // [610, 987, true]
q