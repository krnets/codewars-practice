// 6kyu - Fibonacci, Tribonacci and friends

// function Xbonacci(signature, n) {
//     let res = [...signature]

//     for (let i = 0; i < n; i++) {
//         res.push(
//             res.slice(i, i + signature.length)
//             .reduce((a, b) => a + b))
//     }
//     return res.slice(0, n)
// }

// function Xbonacci(signature, n) {
//     let len = signature.length
//     for (let i = len; i < n; i++)
//         signature[i] = signature.slice(i - len).reduce((a, b) => a + b)
//     return signature.slice(0, n)
// }

// function Xbonacci(signature, n) {
//     for (let x = signature.length, i = 0; i < n - x; i++)
//         signature.push(signature.slice(i, x + i).reduce((a, b) => a + b))

//     return signature.slice(0, n)
// }

// function Xbonacci(signature, n) {
//     const res = signature.slice(0, n)
//     while (res.length < n)
//         res.push(res.slice(-signature.length).reduce((a, b) => a + b))
//     return res
// }

const Xbonacci = (s, n, l = s.length) => s.length >= n ? s.slice(0, n) : Xbonacci([...s, eval(s.slice(-l).join `+`)], n, l)


q = Xbonacci([0, 1], 10) // [0,1,1,2,3,5,8,13,21,34]
q
q = Xbonacci([1, 1], 10) // [1,1,2,3,5,8,13,21,34,55]
q
q = Xbonacci([0, 0, 0, 0, 1], 10) // [0,0,0,0,1,1,2,4,8,16]
q
q = Xbonacci([1, 0, 0, 0, 0, 0, 1], 10) // [1,0,0,0,0,0,1,2,3,6]
q
q = Xbonacci([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20) // [1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256]
q