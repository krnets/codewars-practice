// 7kyu - Growth of a Population

// function nbYear(p0, percent, aug, p) {
//     let curY = p0 + p0 * (percent / 100) + aug
//     for (var years = 1; years < p; years++) {
//         curY = curY + curY * (percent / 100) + aug
//         if (curY >= p)
//             return years + 1
//     }
// }

// function nbYear(p0, percent, aug, p) {
//     for (var year = 0; p0 < p; year++)
//         p0 = p0 + p0 * (percent / 100) + aug
//     return year
// }

// const nbYear = (p0, percent, aug, p) => (p0 < p) ? 1 + nbYear(p0 + p0 * (percent / 100) + aug, percent, aug, p) : 0
const nbYear = (p0, percent, aug, p) => (p0 < p) ? 1 + nbYear(p0 * (1 + percent / 100) + aug, percent, aug, p) : 0

q = nbYear(1500, 5, 100, 5000) // 15
q
q = nbYear(1500000, 2.5, 10000, 2000000) // 10
q
q = nbYear(1500000, 0.25, 1000, 2000000) // 94
q