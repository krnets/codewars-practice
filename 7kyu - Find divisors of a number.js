// const getDivisorsCnt = n => Array(n).fill()
//     .map((_, i) => i + 1)
//     .filter(i => n % i == 0)
//     .length

// const factors = x => Number.isInteger(x) && x > 0 ?
// .reverse() : -1

// if (typeof x == 'number' && x > 0 && Number.isInteger(x)) {
// if (x == parseInt(x, 10) && x > 0) {
// if (Number.isInteger(x) && x > 0) {

// function getDivisorsCnt(x) {
//     let result = []
//     let i = x
//     while (i > 0) {
//         if (x % i == 0)
//             result.push(i)
//         i--
//     }
//     return result.length
// }

function getDivisorsCnt(n) {
    for (var divisors = 0, i = n; i > 0; i--)
        if (n % i == 0) divisors++
    return divisors
}

// function getDivisorsCnt(n) {
//     for (var d = 0, i = n; i > 0; i--)
//         if (n % i == 0) d++
//     return d
// }

q = getDivisorsCnt(1) // 1
q
q = getDivisorsCnt(10) // 4
q
q = getDivisorsCnt(11) // 2
q
q = getDivisorsCnt(54) // 8
q