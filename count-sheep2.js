// var countSheep = function (num) {
//     let output = ''
//     for (let i = 1; i <= num; i++) {
//         output += `${i} sheep...`
//     }
//     return output
// }

// return [...Array(n)].map((_, index) => index + 1 + ' sheep...').join('')

let countSheep = n => [...Array(n)].map((_,index) => `${index + 1} sheep...`).join``


q = countSheep(1) // "1 sheep...");
q
q = countSheep(2) // "1 sheep...2 sheep...");
q
q = countSheep(3) // "1 sheep...2 sheep...3 sheep...");
q