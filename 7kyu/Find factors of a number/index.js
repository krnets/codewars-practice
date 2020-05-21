// const factors = x => !!x ? Array(x).fill(0)
//     .map((_, i) => i + 1)
//     .filter((_, i) => Math.floor(x % (i + 1) == 0))
//     .reverse() : []

// function factors(x) {
//     if (typeof x != 'number' || x < 1 || !Number.isInteger(x))
//         return -1

//     let result = []

//     for (let i = x; i > 0; i--)
//         if (x % i == 0)
//             result.push(i)

//     return result
// }


// function factors(x) {
//     // if (typeof x == 'number' && x > 0 && Number.isInteger(x)) {
//     // if (x == parseInt(x, 10) && x > 0) {
//     if (Number.isInteger(x) && x > 0) {

//         let result = []
//         let i = x

//         while (i > 0) {
//             if (x % i == 0)
//                 result.push(i)
//             i--
//         }
//         return result
//     }
//     return -1
// }

// const factors = number => {
//     const factorsFound = Array.from({
//             length: number + 1
//         }, (_, index) => index)
//         .filter(index => number % index === 0)
//         .reverse()

//     return factorsFound.length ? factorsFound : -1
// }

const factors = x => Number.isInteger(x) && x > 0 ?
    Array(x).fill()
    .map((_, i) => i + 1)
    .filter(i => x % i == 0)
    .reverse() : -1

q = factors(54) // [54,27,18,9,6,3,2,1]
q
q = factors(9) // [9,3,1]
q
q = factors()
q
q = factors(0)
q