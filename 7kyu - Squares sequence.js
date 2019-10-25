// 7kyu - Squares sequence

// function squares(x, n) {
//     if (n < 1) {
//         return []
//     }

//     let result = x
//     let arr = []
//     arr.push(x)

//     for (let i = 0; i < n - 1; i++) {
//         result = result * result
//         arr.push(result)
//     }
//     return arr
// }


// function squares(x, n) {
//     let arr = []

//     for (let i = 0; i < n; i++) {
//         arr.push(x)
//         x *= x
//     }
//     return arr
// }


const squares = (x, n) => (n < 1) ? [] : Array(n).fill(0).map((_, index) => Math.pow(x, Math.pow(2, index)))