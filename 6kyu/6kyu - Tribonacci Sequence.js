// 6kyu - Tribonacci Sequence

// function tribonacci(signature, n) {
//     if (n < signature.length)
//         return (n === 0) ? [] : signature.slice(0, n)

//     for (let i = signature.length; i < n; i += 1)
//         signature.push(signature[i - 1] + signature[i - 2] + signature[i - 3])

//     return signature
// }

// function tribonacci(signature, n) {
//     let res = [...signature]
//     for (let i = 0; i < n; i++)
//         res.push(res.slice(i, i + 3).reduce((acc, next) => acc + next))
//     return res.slice(0, n)
// }

// function tribonacci(signature, n) {
//     for (let i = 3; i < n; i++)
//         signature[i] = signature[i - 1] + signature[i - 2] + signature[i - 3]

//     return signature.slice(0, n)
// }

// function tribonacci(signature, n) {
//     while (signature.length < n)
//         signature.push(signature.slice(-3).reduce((a, b) => a + b))

//     return signature.slice(0, n)
// }

function tribonacci(signature, n) {
    let a = signature.splice(0, n)

    for (let i = 3; i < n; i++)
        a.push(a[i-3] + a[i-2] + a[i-1])

    return a
}


q = tribonacci([1, 1, 1], 10) // [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
q
q = tribonacci([0, 0, 1], 10) // [0,0,1,1,2,4,7,13,24,44]
q
q = tribonacci([0, 1, 1], 10) // [0,1,1,2,4,7,13,24,44,81]
q
q = tribonacci([1, 0, 0], 10) // [1,0,0,1,1,2,4,7,13,24]
q
q = tribonacci([0, 0, 0], 10) // [0,0,0,0,0,0,0,0,0,0]
q
q = tribonacci([1, 2, 3], 10) // [1,2,3,6,11,20,37,68,125,230]
q
q = tribonacci([3, 2, 1], 10) // [3,2,1,6,9,16,31,56,103,190]
q
q = tribonacci([1, 1, 1], 1) // [1]
q
q = tribonacci([300, 200, 100], 0), []
q
q = tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]
q