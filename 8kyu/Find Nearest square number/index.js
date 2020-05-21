// 8kyu - Find Nearest square number

// Find the nearest square number, nearest_sq(n), of a positive integer n.

// function nearestSq(n) {
//     let res = []
//     for (let i = 0; i < n; i++) {
//         let square = i * i
//         res.push(square)
//         if (square > n) {
//             break
//         }
//     }
//     let r = res.slice(-2)
//     let s = r.map(v => Math.abs(n - v))
//     return s.length > 1 ? s[0] < s[1] ? r[0] : r[1] : n
// }

const nearestSq = n => Math.pow(Math.round(Math.sqrt(n)), 2)

q = nearestSq(1) // 1
q
q = nearestSq(2) // 1
q
q = nearestSq(10) // 9
q
q = nearestSq(111) // 121
q
q = nearestSq(9999) // 10000
q