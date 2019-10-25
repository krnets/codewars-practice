// const countBy = (x, n) => Array.from({length: n + 1}, (_, i) => i * x).slice(1)
// const countBy = (x, n) => Array.from({length: n}, (_, i) => (i + 1) * x)

// function countBy(x, n) {
//     let z = []

//     for (let i = 1; i < n; i++) {
//         z.push(x * i)
//     }
//     return z
// }

// function countBy(x,n) {
//     for (var z = [], i = 0; i < n; i++) {
//         z.push(x * (1 + i))
//     }
//     return z
// }

function countBy(x,n) {
    let z = []

    while (z.length < n)  {
        z.push(x * (z.length + 1))
    }
    return z    
}

q = countBy(1, 5) //, [1,2,3,4,5], "Array does not match")
q
// q = countBy(2, 5) // [2,4,6,8,10], "Array does not match")
// q